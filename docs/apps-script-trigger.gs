/**
 * SPAR F26 — fire the GitHub sync the moment someone edits this sheet.
 *
 * SETUP (one time, ~3 minutes, must be done by someone with edit access to the sheet)
 * ---------------------------------------------------------------------------
 * 1. Open the sheet -> Extensions -> Apps Script.
 * 2. Delete whatever is in Code.gs and paste this whole file.
 * 3. Left sidebar -> Project Settings (gear) -> Script Properties -> Add:
 *      GITHUB_TOKEN  = a GitHub *fine-grained* personal access token
 *      GITHUB_REPO   = webdevsha/spar-f26-id
 *    The token needs exactly ONE permission:
 *      Repository permissions -> Actions: Read and write   (nothing else)
 *    and it must be scoped to that single repository only.
 * 4. Left sidebar -> Triggers (clock icon) -> Add Trigger:
 *      function: onSheetChange
 *      event source: From spreadsheet
 *      event type: On change
 *      failure notification: Notify me immediately
 * 5. Approve the permission prompt (it needs to call the external URL).
 * 6. Test: type something in any cell, then check
 *      https://github.com/webdevsha/spar-f26-id/actions
 *    A "sync-sheets" run should appear within seconds.
 *
 * SECURITY NOTE — read this.
 * ---------------------------------------------------------------------------
 * The GitHub token lives in Google's Script Properties, readable by anyone who
 * can edit this Apps Script project (i.e. the sheet's editors). Keep it
 * fine-grained and limited to Actions:write on this one repo so the worst case
 * is "someone can trigger a sync", not "someone can read or push code".
 * Rotate it if a collaborator leaves the project.
 */

var PROPS = PropertiesService.getScriptProperties();

function onSheetChange(e) {
  var token = PROPS.getProperty('GITHUB_TOKEN');
  var repo = PROPS.getProperty('GITHUB_REPO');
  if (!token || !repo) {
    console.error('GITHUB_TOKEN / GITHUB_REPO not set in Script Properties.');
    return;
  }

  // Who made the change. On a plain edit this is the editor's email; on a
  // change event with no user (e.g. an API write) it falls back to unknown.
  var editor = '';
  try {
    editor = Session.getActiveUser().getEmail() || '';
  } catch (err) {
    editor = '';
  }

  var payload = {
    event_type: 'sheet-change',
    client_payload: {
      editor: editor,
      source: 'sheet edit (real-time trigger)',
      at: new Date().toISOString()
    }
  };

  var response = UrlFetchApp.fetch('https://api.github.com/repos/' + repo + '/dispatches', {
    method: 'post',
    contentType: 'application/json',
    headers: {
      Authorization: 'Bearer ' + token,
      Accept: 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28'
    },
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  });

  var code = response.getResponseCode();
  if (code !== 204) {
    console.error('GitHub dispatch failed (' + code + '): ' + response.getContentText());
  }
}
