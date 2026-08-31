from flask import Flask, render_template, request

def create_app():
    """Application factory function for testing"""
    app = Flask(__name__)
    app.config['TESTING'] = False
    
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/add', methods=['POST'])
    def add():
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        addition = num1 + num2
        return render_template('index.html', sum=addition)

    @app.route('/api/health', methods=['GET'])
    def health():
        """Health check endpoint for CI/CD monitoring"""
        return {'status': 'healthy', 'message': 'Flask app is running'}, 200

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
