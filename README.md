<h1>AI Chatbot with OpenAI GPT</h1>

<p>This repository contains a Django-based AI chatbot leveraging the OpenAI GPT models.</p>
    
<h2>Chat Session Storage:</h2>
<p><strong>Note:</strong> All chat sessions are saved for improving user experience and future enhancements. Please be aware of this when interacting with the chatbot.</p>

<h2>Note on OpenAI API Subscription:</h2>

<p>This current version of the project does not use a premium subscription for the OpenAI API. Therefore, the chatbot will often respond with:</p>
    <blockquote>
<p>"We're currently on a limited OpenAI plan. For extended features and uninterrupted responses, please consider upgrading the API plan. Thanks for understanding!"</p>
    </blockquote>

<p>If you have a premium subscription for OpenAI GPT or if you're planning to subscribe, you can easily integrate it with this chatbot. Follow the instructions below to set up:</p>
    
<h2>Project Dashboard:</h2>
<p>You can also check out our project dashboard for more insights. </p>
<img src="https://github.com/romanhumagain/AI-Chat-Bot/blob/master/AI_Chatbot/chatbot/static/images/application-dashboard.png" alt="Project Dashboard Preview" width="600">


<h2>Setup:</h2>

<ol>
<li>Clone this repository:</li>
<pre><code>git clone &lt;repository-link&gt;</code></pre>

<li>Navigate to the project directory:</li>
<pre><code>cd path-to-project</code></pre>

<li>Install the required packages:</li>
<pre><code>pip install -r requirements.txt</code></pre>

<li>Set up your OpenAI API key:
<ul>
<li>Obtain your API key from the OpenAI dashboard.</li>
<li>In the project, locate the spot where the API key should be set (search for a placeholder or comment indicating where to place the API key).</li>
<li>Replace the placeholder with your actual API key.</li>
</ul>
</li>

<li>Run the Django migrations:</li>
<pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>

<li>Start the Django development server:</li>
<pre><code>python manage.py runserver</code></pre>

<li>Visit <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a> in your browser to interact with the chatbot!</li>
</ol>

<h2>Contributions:</h2>

<p>Feel free to fork this repository, make improvements, and create pull requests. Any contributions are welcome!</p>

    
