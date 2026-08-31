from flask import Flask, render_template, request

def create_app():
    """Application factory function for testing"""
    app = Flask(__name__)
    app.config['TESTING'] = False
    
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/greet', methods=['POST'])
    def greet():
        name = request.form.get('name', 'Friend')
        message = f"Hi, {name}! Welcome to Flask!"
        return render_template('index.html', greeting=message)

    @app.route('/api/health', methods=['GET'])
    def health():
        """Health check endpoint for CI/CD monitoring"""
        return {'status': 'healthy', 'message': 'Flask app is running'}, 200

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
