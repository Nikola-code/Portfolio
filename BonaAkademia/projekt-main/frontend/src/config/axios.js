import axios from "axios";

axios.defaults.baseURL = import.meta.env.VITE_APP_API_URL;

axios.interceptors.request.use(
  (config) => {
    const token = JSON.parse(sessionStorage.getItem("access_token"));
    if (token) {
      config.headers.authorization = `Bearer ${token}`;
      config.headers.accept = "application/json";
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

axios.interceptors.response.use(
  (response) => {
    if (response.status >= 200 && response.status < 300) {
      return Promise.resolve(response);
    } else {
      return Promise.reject(response);
    }
  },
  (error) => {
    if (
      error.response.status === 401 ||
      error.response.status === 302 ||
      error.response.status === 403
    ) {
      // TODO dorzucić obsługę wylogowywania jak będzie obsłużona autoryzacja
    } else {
      return Promise.reject(error);
    }
  }
);

export default axios;
