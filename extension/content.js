chrome.runtime.onMessage.addListener(
    function (request, sender, sendResponse) {
      if (request.action === "checkWebsite" && chrome.storage.sync.get('isEnabled', function (data) { sendResponse(data.isEnabled); })) {
        checkWebsite();
      }
    }
  );
  
  function checkWebsite() {
    try {
      // You can add additional checks here based on the webpage content, if needed
      // For simplicity, this example checks for a specific error message related to certificate authority
  
      const errorMessage = "NET::ERR_CERT_AUTHORITY_INVALID";
  
      if (document.documentElement.innerHTML.includes(errorMessage)) {
        // Certificate error detected, take action (e.g., redirect to DuckDuckGo)
        chrome.tabs.update({ url: "https://www.duckduckgo.com" });
      }
    } catch (error) {
      console.error("Error: " + error.message);
    }
  }
  