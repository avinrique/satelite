chrome.webNavigation.onErrorOccurred.addListener(function (details) {
    chrome.tabs.sendMessage(details.tabId, { action: 'checkWebsite' });
  }, { url: [{ schemes: ['http', 'https'] }] });
  