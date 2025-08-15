css = '''
<style>
body {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%);
    color: #e2e8f0;
    margin: 0;
    padding: 0;
    line-height: 1.6;
}

.container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 2rem;
}

.header-container {
    background: #2d3748;
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    margin-bottom: 2.5rem;
    box-shadow: 0 8px 24px rgb(58, 58, 168);
    border: 1px solid blue;
}

.header-container h1 {
    font-size: 1.9rem;
    font-weight: 800;
    color: #3b82f6;
    margin: 0;
    letter-spacing: -0.025em;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
}

.header-container p {
    font-size: 1.2rem;
    color: #94a3b8;
    margin-top: 0.25rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

.books-emoji {
    font-size: 1.6rem;
    vertical-align: middle;
    line-height: 1;
}

.welcome-box {
    border-radius: 1rem;
    padding: 2.5rem;
    text-align: center;
    margin-bottom: 2.5rem;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    animation: fadeIn 0.8s ease-in;
    border: 1px solid #334199;
}

.welcome-box h2 {
    font-size: 2rem;
    color: #f1f5f9;
    margin: 0 0 1rem;
}

.welcome-box p {
    font-size: 1.1rem;
    color: #94a3b8;
    max-width: 500px;
    margin: 0 auto;
}

.input-container {
    display: flex;
    gap: 1rem;
    margin-bottom: 2.5rem;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

.input-container input {
    flex: 1;
    padding: 1rem 1.5rem;
    border: none;
    border-radius: 0.75rem;
    background: #2d3748;
    color: #f1f5f9;
    font-size: 1rem;
    outline: none;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.input-container input:focus {
    background: #374151;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
}

.input-container button {
    padding: 1rem 2rem;
    border: none;
    border-radius: 0.75rem;
    background: linear-gradient(90deg, #3b82f6 0%, #60a5fa 100%);
    color: #fff;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.input-container button:hover {
    background: linear-gradient(90deg, #2563eb 0%, #3b82f6 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
}

.input-container button:active {
    transform: translateY(0);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.question-answer {
    padding: 1.5rem;
    border-radius: 1rem;
    margin-bottom: 1.5rem;
    background: #2d3748;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    animation: slideIn 0.5s ease-out;
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
}

.question {
    font-size: 1.3rem;
    font-weight: 600;
    color: #60a5fa;
    margin-bottom: 1rem;
}

.answer {
    font-size: 1rem;
    color: #e2e8f0;
    line-height: 1.6;
}

.thinking {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0.6rem;
    margin: 2.5rem 0;
}

.thinking span {
    width: 12px;
    height: 12px;
    background: #3b82f6;
    border-radius: 50%;
    animation: bounce 1s infinite;
}

.thinking span:nth-child(2) {
    animation-delay: 0.2s;
}

.thinking span:nth-child(3) {
    animation-delay: 0.4s;
}

.sidebar {
    background: #1e293b;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    border: 1px solid #334155;
}

.sidebar h2 {
    font-size: 1.8rem;
    color: #3b82f6;
    margin-bottom: 1.5rem;
    font-weight: 700;
}

.tips-section {
    background: #2d3748;
    padding: 1.5rem;
    border-radius: 0.75rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.tips-section h3 {
    font-size: 1.3rem;
    color: #f1f5f9;
    margin-bottom: 1rem;
    font-weight: 600;
}

.tips-section ul {
    list-style: disc;
    padding-left: 1.5rem;
    color: #94a3b8;
    font-size: 0.95rem;
}

.tips-section li {
    margin-bottom: 0.75rem;
}

.file-uploader {
    margin-bottom: 1.5rem;
}

.submit-button {
    width: 100%;
    padding: 1rem;
    border: none;
    border-radius: 0.75rem;
    background: linear-gradient(90deg, #3b82f6 0%, #60a5fa 100%);
    color: #fff;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.submit-button:hover {
    background: linear-gradient(90deg, #2563eb 0%, #3b82f6 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
}

.submit-button:active {
    transform: translateY(0);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes slideIn {
    from { transform: translateY(20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-12px); }
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
