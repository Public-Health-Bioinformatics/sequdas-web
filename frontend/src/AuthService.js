export default class AuthService {

    constructor(domain) {
	
    }

    login(username, password) {
        
    }

    loggedIn() {
        
    }

    isTokenExpired(token) {
        
    }

    setToken(idToken) {
        // Saves user token to localStorage
        localStorage.setItem(this.token_storage_key, idToken)
    }

    getToken() {
        // Retrieves the user token from localStorage
        return localStorage.getItem(this.token_storage_key)
    }

    logout() {
        // Clear user token and profile data from localStorage
        localStorage.removeItem(this.token_storage_key);
	return Promise.resolve(localStorage.getItem(this.token_storage_key));
    }

    getProfile() {
        
    }


    fetch(url, options) {
        // performs api calls sending the required authentication headers
        const headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        // Setting Authorization header
        // Authorization: Bearer xxxxxxx.xxxxxxxx.xxxxxx
        if (this.loggedIn()) {
	    console.log(this.getToken())
            headers['Authorization'] = 'Bearer ' + this.getToken()
        }

        return fetch(url, {
            headers,
            ...options
        })
            .then(this._checkStatus)
            .then(response => response.json())
    }

    _checkStatus(response) {
        // raises an error in case response status is not a success
        if (response.status >= 200 && response.status < 300) { // Success status lies between 200 to 300
            return response
        } else {
            var error = new Error(response.statusText)
            error.response = response
            throw error
        }
    }
}
