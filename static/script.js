function openModal(username, content, timestamp) {
    document.getElementById("modal-username").textContent = username;
    document.getElementById("modal-content").textContent = content;
    document.getElementById("modal-timestamp").textContent = timestamp;
    document.getElementById("tweetModal").style.display = "block";
  }
  
  function closeModal() {
    document.getElementById("tweetModal").style.display = "none";
  }