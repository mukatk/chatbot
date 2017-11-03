var form = new Vue({
    el: '#chat-wrapper',
    data: {
        mensagens: [],
        mensagem: ''
    },
    methods: {
        enviaMensagem: function (e) {
            const _self = this;
            var objMensagem = {
                texto: _self.mensagem ,
                remetente: true
            };

            _self.mensagens.push(objMensagem);

            _self.$http.get('/chat', { texto: _self.mensagem }).then(response => {
                var objResposta = {
                    texto: response.body,
                    remetente: false
                }
                _self.mensagens.push(objResposta);
            });

            _self.mensagem = '';
        }
    }
});