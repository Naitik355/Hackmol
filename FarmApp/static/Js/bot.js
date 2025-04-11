function toggleChat() {
    const chat = document.getElementById('chatbot-container');
    chat.style.display = chat.style.display === 'none' || chat.style.display === '' ? 'block' : 'none';}
  
    const API_KEY = "AIzaSyCY4XMNJnRoewWgClTqRIAbeE7IzBD0n-A"; // Replace with your actual Gemini API key
    const API_URL = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key=AIzaSyCY4XMNJnRoewWgClTqRIAbeE7IzBD0n-A`;

  const predefinedResponses = {
      "hi": "Hello! How can I assist you?",
      "who are you": "I am a chatbot powered by Google Gemini AI.",
      "bye": "Goodbye! Have a great day!"
  };
  
  // Function to send message
  async function sendMessage() {
      let userInput = document.getElementById("user-input").value.trim();
      if (userInput === "") return;
  
      let chatBox = document.getElementById("chat-box");
  
      // Display user message
      let userMessage = document.createElement("div");
      userMessage.classList.add("user-message");
      userMessage.innerText = userInput;
      chatBox.appendChild(userMessage);
      document.getElementById("user-input").value = "";
      chatBox.scrollTop = chatBox.scrollHeight;
  
      // Check predefined responses first
      if (predefinedResponses[userInput.toLowerCase()]) {
          displayBotMessage(predefinedResponses[userInput.toLowerCase()]);
          return;
      }
  
      // Display "Thinking..." message
      let botMessage = document.createElement("div");
      botMessage.classList.add("bot-message");
      botMessage.innerText = "Thinking...";
      chatBox.appendChild(botMessage);
      chatBox.scrollTop = chatBox.scrollHeight;
  
      try {
          let response = await fetch(API_URL, {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ contents: [{ parts: [{ text: userInput }] }] })
          });
  
          let data = await response.json();
  
          if (data && data.candidates && data.candidates.length > 0 &&
              data.candidates[0].content && data.candidates[0].content.parts.length > 0) {
              botMessage.innerText = data.candidates[0].content.parts[0].text;
          } else {
              botMessage.innerText = "Sorry, I couldn't generate a response.";
          }
      } catch (error) {
          botMessage.innerText = "Error: Unable to connect to AI.";
          console.error("API Error:", error);
      }
  }
  
  // Function to display bot messages
  function displayBotMessage(message) {
      let chatBox = document.getElementById("chat-box");
      let botMessage = document.createElement("div");
      botMessage.classList.add("bot-message");
      botMessage.innerText = message;
      chatBox.appendChild(botMessage);
      chatBox.scrollTop = chatBox.scrollHeight;
  }
  
  // Send message when Enter is pressed
  function handleKeyPress(event) {
      if (event.key === "Enter") {
          sendMessage();
      }
  }