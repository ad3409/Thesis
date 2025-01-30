import React, { useState } from 'react';
import "../styles/AIChat.css"

const ChatComponent = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleInputChange = (event) => {
    setInput(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!input.trim()) return;

    const newMessage = {
      id: messages.length + 1,
      text: 'You: ' + input,
      sender: 'user'
    };

    setMessages(prevMessages => [...prevMessages, newMessage]);

    try {
      const response = await fetch('http://localhost:8000/chat/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input })
      });
      const data = await response.json();
      const aiResponse = {
        id: messages.length + 2,
        text: data.response,
        sender: 'ai'
      };

      setMessages(prevMessages => [...prevMessages, aiResponse]);
    } catch (error) {
      console.error('Error:', error);
    }

    setInput('');
  };

  return (
    <div style={{ textAlign: "center" }}>
      <h4>Ask the AI</h4>
      <div className="chat-container">
        <div className="messages-container">
          {messages.map(message => (
            <div key={message.id} className={`message ${message.sender === 'user' ? 'user-message' : 'ai-message'}`}>
              <div className="message-content">
                {message.text}
              </div>
            </div>
          ))}
        </div>

        <form onSubmit={handleSubmit} style={{ display: 'flex' }}>
          <textarea
            value={input}
            onChange={handleInputChange}
            placeholder='Do you have a question? Type here!'
            className="chat-input"
          />
          <button type="submit" className="send-button">
            Send
          </button>
        </form>
      </div>
    </div>
  );
};

export default ChatComponent;
