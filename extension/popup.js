document.addEventListener('DOMContentLoaded', function () {
    var enableCheckbox = document.getElementById('enableCheckbox');
  
    enableCheckbox.addEventListener('change', function () {
      chrome.storage.sync.set({ 'isEnabled': enableCheckbox.checked });
    });
  });
  