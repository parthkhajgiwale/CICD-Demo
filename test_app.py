import pytest
from app import create_app


@pytest.fixture
def app():
    """Create and configure a test app"""
    app = create_app()
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(app):
    """A test client for the app"""
    return app.test_client()


class TestHome:
    """Tests for the home page"""
    
    def test_home_page_loads(self, client):
        """Test that the home page loads successfully"""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_home_page_contains_title(self, client):
        """Test that home page contains expected content"""
        response = client.get('/')
        assert b'Welcome to Flask' in response.data


class TestAddEndpoint:
    """Tests for the add endpoint"""
    
    def test_add_with_values(self, client):
        """Test add with a value provided"""
        response = client.post('/add', data={'num1': 1, 'num2':3})
        assert response.status_code == 200
        assert b'4' in response.data
    
    def test_add_post_only(self, client):
        """Test that GET request to greet is not allowed"""
        response = client.get('/add')
        assert response.status_code == 405  # Method Not Allowed


class TestHealthCheck:
    """Tests for the health check endpoint"""
    
    def test_health_check_returns_200(self, client):
        """Test that health check returns 200 status"""
        response = client.get('/api/health')
        assert response.status_code == 200
    
    def test_health_check_returns_json(self, client):
        """Test that health check returns valid JSON"""
        response = client.get('/api/health')
        json_data = response.get_json()
        assert json_data is not None
        assert json_data['status'] == 'healthy'
    
    def test_health_check_has_message(self, client):
        """Test that health check includes a message"""
        response = client.get('/api/health')
        json_data = response.get_json()
        assert 'message' in json_data
        assert json_data['message'] == 'Flask app is running'


class TestAppFactory:
    """Tests for the app factory function"""
    
    def test_create_app_returns_flask_app(self):
        """Test that create_app returns a Flask app instance"""
        app = create_app()
        assert app is not None
        assert hasattr(app, 'run')
        assert hasattr(app, 'test_client')
