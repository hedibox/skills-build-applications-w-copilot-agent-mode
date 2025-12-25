// Ce fichier permet de configurer l'URL du WebSocket pour le hot reload dans un environnement cloud comme GitHub Codespaces ou devcontainer.

module.exports = {
  devServer: {
    host: '0.0.0.0',
    port: 3000,
    client: {
      webSocketURL: {
        hostname: 'localhost',
        port: 3000,
        protocol: 'ws',
      },
    },
  },
};
