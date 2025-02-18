import React, { useState } from 'react';
import "../styles/AIChat.css";
 
const ChatComponent = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [fuzzyScores, setFuzzyScores] = useState({
    Dignity: 5,
    Trust: 5,
    Responsibility: 5,
    Domination: 5,
    Justice: 5,
    Privacy: 5,
    Truth: 5,
    Inequality: 5,
    Autonomy: 5,
    Exclusion: 5,
    Exploitation: 5,
  });
  const [ethicalScore, setEthicalScore] = useState(0);
 
  const handleInputChange = (event) => {
    setInput(event.target.value);
  };
 
  const handleFuzzyChange = (feature, value) => {
    setFuzzyScores((prevScores) => ({ ...prevScores, [feature]: Number(value) }));
  };
 
  const calculateEthicalScore = () => {
    const totalScore = Object.values(fuzzyScores).reduce((sum, value) => sum + value, 0);
    const avgScore = totalScore / Object.keys(fuzzyScores).length;
 
    let adjustedScore = avgScore;
    if (avgScore > 8) {
      adjustedScore = avgScore * 1.1;
    } else if (avgScore < 4) {
      adjustedScore = avgScore * 0.9;
    }
 
    setEthicalScore(Math.min(10, adjustedScore.toFixed(2)));
  };
 
  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) return;
 
    const newMessage = {
      id: messages.length + 1,
      text: 'You sent an image.',
      sender: 'user',
      image: URL.createObjectURL(file),
    };
 
    setMessages((prevMessages) => [...prevMessages, newMessage]);
 
    const aiResponse = {
      id: messages.length + 2,
      text: "AI: I see you sent an image!",
      sender: 'ai',
    };
 
    setMessages((prevMessages) => [...prevMessages, aiResponse]);
  };
 
  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!input.trim()) return;
 
    const newMessage = {
      id: messages.length + 1,
      text: 'You: ' + input,
      sender: 'user',
    };
 
    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setLoading(true);
 
    try {
      const response = await fetch('http://localhost:8000/chat/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input }),
      });
      const data = await response.json();
      const aiResponse = {
        id: messages.length + 2,
        text: data.response,
        sender: 'ai',
      };
 
      setMessages((prevMessages) => [...prevMessages, aiResponse]);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
 
    setInput('');
  };
 
  return (
    <div>
      <p><strong>Disclaimer:</strong> Responses provided by this chatbot may not be accurate. Please verify independently.</p>
 
      <div style={{ textAlign: "center" }}>
        <h4>Ask the EthicalAI</h4>
        <div className="chat-container" style={{ marginRight: 'auto', marginLeft: 'auto', maxWidth: '800px' }}>
          <div className="messages-container">
            {messages.map((message) => (
              <div
                key={message.id}
                className={`message ${message.sender === 'user' ? 'user-message' : 'ai-message'}`}
              >
                <div className="message-content">
                  {message.text}
                  {message.image && (
                    <img
                      src={message.image}
                      alt="Uploaded"
                      className="uploaded-image"
                      style={{ maxWidth: '200px', maxHeight: '200px', borderRadius: '8px', marginTop: '10px' }}
                    />
                  )}
                </div>
              </div>
            ))}
            {loading && (
              <div className="loading-indicator">
                <span>Loading...</span>
              </div>
            )}
          </div>
 
          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', padding: '20px', fontSize: '1.2rem' }}>
            <textarea
              value={input}
              onChange={handleInputChange}
              placeholder="Do you have a question? Type here!"
              className="chat-input"
              style={{ height: '100px', fontSize: '1.2rem', padding: '10px' }}
            />
            <div style={{ display: 'flex', alignItems: 'center', marginTop: '10px' }}>
              <input
                type="file"
                accept="image/*"
                onChange={handleFileUpload}
                className="file-input"
                style={{ marginRight: '10px', fontSize: '1.1rem' }}
              />
              <button type="submit" className="send-button" style={{ fontSize: '1.2rem', padding: '10px 20px' }}>
                Send
              </button>
            </div>
          </form>
        </div>
 
        {/* Repositioned Fuzzy Scale */}
        <div style={{
          marginTop: '200px', // Significant margin to move it farther below
          padding: '10px',
          border: '1px solid #ccc',
          borderRadius: '8px',
          backgroundColor: '#f9f9f9',
          maxWidth: '800px',
          marginLeft: 'auto',
          marginRight: 'auto',
        }}>
          <h5>Fuzzy Scale</h5>
          <ul style={{ listStyleType: 'none', padding: 0 }}>
            {Object.keys(fuzzyScores).map((feature) => (
              <li key={feature} style={{ marginBottom: '10px' }}>
                {feature}:
                <input
                  type="range"
                  min="0"
                  max="10"
                  value={fuzzyScores[feature]}
                  onChange={(e) => handleFuzzyChange(feature, e.target.value)}
                  style={{ marginLeft: '10px' }}
                />
              </li>
            ))}
          </ul>
          <button
            onClick={calculateEthicalScore}
            style={{ marginTop: '10px', padding: '10px', fontSize: '1rem', cursor: 'pointer' }}
          >
            Calculate Ethical Score
          </button>
          <div style={{ marginTop: '10px' }}>
            <strong>Ethical Score:</strong>
            <input
              type="text"
              value={ethicalScore}
              readOnly
              style={{ marginLeft: '10px', width: '50px', textAlign: 'center' }}
            />
          </div>
        </div>
      </div>
 
      <div className="footer">
        © {new Date().getFullYear()} Developed by <a href="https://www.linkedin.com/in/alamin-dhali/" target="_blank"rel="noopener noreferrer">Al Amin Dhali</a>
      </div>
    </div>
  );
};
 
export default ChatComponent;
