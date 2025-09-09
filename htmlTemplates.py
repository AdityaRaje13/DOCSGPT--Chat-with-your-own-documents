# htmlTemplates.py
# Modern HTML and CSS templates for DocsGPT UI with Dark/Light Mode

css_template = """
    .stApp {
        background: var(--bg-secondary);
        transition: all 0.3s ease;
    }
    
    .stApp > header {
        background-color: transparent;
    }
    
    .main .block-container {
        padding: 1.5rem;
        max-width: 1200px;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    
    /* Main Header */
    .modern-header {
        background: var(--bg-primary);
        border-radius: 20px;
        padding: 2.5rem;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 6px 22px blue;
        border: 1px solid var(--border);
        position: relative;
        overflow: hidden;
        margin-top: -4rem;
    }
    
    .modern-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899, #f59e0b);
        # box-shadow: 5px 5px 5px blue;
    }
    
    .modern-header h1 {
        font-family: 'Inter', sans-serif;
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        margin-top: -1.5rem;
        background: linear-gradient(135deg, var(--accent), #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 1rem;
    }
    
    .modern-header p {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        color: var(--text-secondary);
        margin: 0;
        font-weight: 500;
    }
    
    .books-emoji {
        font-size: 2.5rem;
        animation: bounce 2s infinite;
    }
    
    /* Input Container */
    .input-section {
        background: var(--bg-primary);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px var(--shadow);
        border: 1px solid var(--border);
    }
    
    .input-wrapper {
        display: flex;
        gap: 1rem;
        align-items: end;
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* Welcome Container */
    .welcome-container {
        background: var(--bg-primary);
        border-radius: 20px;
        padding: 1rem 3rem;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px var(--shadow);
        border: 1px solid var(--border);
        position: relative;
        overflow: hidden;
    }
    
    .welcome-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(59, 130, 246, 0.1), transparent);
        animation: shimmer 3s infinite;
        pointer-events: none;
    }
    
    .welcome-container h2 {
        font-family: 'Inter', sans-serif;
        font-size: 2.2rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
        position: relative;
    }
    
    .welcome-container p {
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        color: var(--text-secondary);
        margin: 0;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
        position: relative;
    }
    
    .welcome-features {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin-top: 2rem;
        position: relative;
    }
    
    .feature-card {
        background: var(--bg-secondary);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid var(--border);
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px var(--shadow);
    }
    
    .feature-icon {
        font-size: 2rem;
        color: var(--accent);
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
    }
    
    .feature-desc {
        font-size: 0.9rem;
        color: var(--text-secondary);
        line-height: 1.4;
    }
    
    /* Chat Container */
    .chat-container {
        background: var(--bg-primary);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px var(--shadow);
        border: 1px solid var(--border);
        max-height: 60vh;
        overflow-y: auto;
        scrollbar-width: thin;
        scrollbar-color: var(--accent) transparent;
    }
    
    .chat-container::-webkit-scrollbar {
        width: 6px;
    }
    
    .chat-container::-webkit-scrollbar-track {
        background: transparent;
    }
    
    .chat-container::-webkit-scrollbar-thumb {
        background: var(--accent);
        border-radius: 3px;
    }
    
    .chat-container::-webkit-scrollbar-thumb:hover {
        background: var(--accent);
        opacity: 0.8;
    }
    
    /* Chat Message Styles */
    .chat-message {
        display: flex;
        margin-bottom: 1rem;
        align-items: flex-start;
        gap: 1rem;
        animation: slideInUp 0.5s ease-out;
    }
    
    .chat-message.user {
        flex-direction: row-reverse;
    }
    
    .chat-message .avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: var(--accent);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
    }
    
    .chat-message.user .avatar {
        background: #10b981;
    }
    
    .chat-message .message {
        background: var(--bg-secondary);
        padding: 1rem 1.5rem;
        border-radius: 16px;
        color: var(--text-primary);
        border: 1px solid var(--border);
        max-width: 80%;
        line-height: 1.6;
        box-shadow: 0 2px 8px var(--shadow);
    }
    
    .chat-message.user .message {
        background: linear-gradient(135deg, var(--accent), #8b5cf6);
        color: white;
        border: none;
    }
    
    /* Thinking Animation */
    .thinking {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 2rem;
        background: var(--bg-primary);
        border-radius: 16px;
        margin: 2rem 0;
        box-shadow: 0 4px 16px var(--shadow);
        border: 1px solid var(--border);
    }
    
    .thinking-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1.5rem;
    }
    
    .thinking-text {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        color: var(--text-secondary);
        font-weight: 500;
    }
    
    .thinking-dots {
        display: flex;
        gap: 0.5rem;
    }
    
    .thinking-dot {
        width: 12px;
        height: 12px;
        background: var(--accent);
        border-radius: 50%;
        animation: thinking-bounce 1.4s infinite ease-in-out;
    }
    
    .thinking-dot:nth-child(1) { animation-delay: -0.32s; }
    .thinking-dot:nth-child(2) { animation-delay: -0.16s; }
    
    .thinking-progress {
        width: 200px;
        height: 4px;
        background: var(--bg-secondary);
        border-radius: 2px;
        overflow: hidden;
        position: relative;
    }
    
    .thinking-progress::before {
        content: '';
        position: absolute;
        left: -50%;
        top: 0;
        width: 50%;
        height: 100%;
        background: linear-gradient(90deg, transparent, var(--accent), transparent);
        animation: thinking-progress 2s infinite;
    }
    
    /* Input Styling */
    .stTextInput > div > div > input {
        background: var(--bg-secondary);
        border: 2px solid var(--border);
        border-radius: 50px;
        padding: 1rem 1.5rem;
        font-size: 1rem;
        font-family: 'Inter', sans-serif;
        color: var(--text-primary);
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px var(--shadow);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--accent);
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
        outline: none;
        transform: translateY(-2px);
    }
    
    .stTextInput > div > div > input::placeholder {
        color: var(--text-secondary);
        font-weight: 400;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, var(--accent), #8b5cf6);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 1rem 2.5rem;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 16px rgba(59, 130, 246, 0.3);
        min-width: 120px;
        height: 56px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(59, 130, 246, 0.4);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: var(--bg-primary);
        border-right: 1px solid var(--border);
    }
    
    
    /* File Uploader */
    .stFileUploader > div {
        border: 2px dashed var(--border);
        border-radius: 16px;
        padding: 2rem;
        background: var(--bg-secondary);
        transition: all 0.3s ease;
        text-align: center;
    }
    
    .stFileUploader > div:hover {
        border-color: var(--accent);
        background: var(--bg-tertiary);
        transform: translateY(-2px);
    }
    
    .stFileUploader label {
        color: var(--text-primary) !important;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        margin-top: 1rem;
    }
    
    /* Sidebar Buttons */
    .css-1d391kg .stButton > button {
        width: 100%;
        margin-top: 1rem;
        background: linear-gradient(135deg, #10b981, #059669);
        box-shadow: 0 4px 16px rgba(16, 185, 129, 0.3);
    }
    
    .css-1d391kg .stButton > button:hover {
        background: linear-gradient(135deg, #059669, #047857);
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
    }
    
    /* Tips Section */
    .tips-section {
        background: var(--bg-secondary);
        border-radius: 16px;
        padding: 1.5rem;
        margin-top: 2rem;
        border: 1px solid var(--border);
        box-shadow: 0 4px 16px var(--shadow);
    }
    
    .tips-section h3 {
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .tips-section h3::before {
        content: '💡';
        font-size: 1.1rem;
    }
    
    .tips-section ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .tips-section li {
        color: var(--text-secondary);
        margin-bottom: 0.75rem;
        padding-left: 1.5rem;
        position: relative;
        line-height: 1.5;
    }
    
    .tips-section li::before {
        content: '✓';
        position: absolute;
        left: 0;
        color: #10b981;
        font-weight: bold;
    }
    
    /* Status Messages */
    .stSuccess, .stError, .stWarning, .stInfo {
        border-radius: 12px;
        padding: 1rem 1.5rem;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        border: none;
        box-shadow: 0 4px 12px var(--shadow);
    }
    
    .stSuccess {
        background: rgba(16, 185, 129, 0.1);
        color: #059669;
        border-left: 4px solid #10b981;
    }
    
    .stError {
        background: rgba(239, 68, 68, 0.1);
        color: #dc2626;
        border-left: 4px solid #ef4444;
    }
    
    .stWarning {
        background: rgba(245, 158, 11, 0.1);
        color: #d97706;
        border-left: 4px solid #f59e0b;
    }
    
    .stInfo {
        background: rgba(59, 130, 246, 0.1);
        color: #2563eb;
        border-left: 4px solid #3b82f6;
    }
    
    /* Spinner */
    .stSpinner > div {
        color: var(--accent);
    }
    
    /* Form styling */
    .stForm {
        background: transparent;
        border: none;
    }
    
    /* Animations */
    @keyframes bounce {
        0%, 20%, 53%, 80%, 100% {
            transform: translate3d(0,0,0);
        }
        40%, 43% {
            transform: translate3d(0, -15px, 0);
        }
        70% {
            transform: translate3d(0, -7px, 0);
        }
        90% {
            transform: translate3d(0, -2px, 0);
        }
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    
    @keyframes slideInUp {
        from {
            transform: translateY(30px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
    
    @keyframes thinking-bounce {
        0%, 80%, 100% {
            transform: scale(0);
        }
        40% {
            transform: scale(1);
        }
    }
    
    @keyframes thinking-progress {
        0% { left: -50%; }
        100% { left: 100%; }
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .modern-header h1 {
            font-size: 2rem;
            flex-direction: column;
            gap: 0.5rem;
        }
        
        .input-wrapper {
            flex-direction: column;
            gap: 1rem;
        }
        
        .stButton > button {
            width: 100%;
        }
        
        .welcome-features {
            grid-template-columns: 1fr;
        }
    }
"""

# Templates remain the same
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
    🤖
    </div>
    <div class="message">{message}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
    👤
    </div>    
    <div class="message">{message}</div>
</div>
'''
