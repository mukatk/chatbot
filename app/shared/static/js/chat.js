var form = new Vue({
    el: '#chat-wrapper',
    data: {
        mensagens: [],
        mensagem: ''
    },
    watch: {
        mensagens: function(mensagemNova) {
            this.goToBottom();
        }
    },
    methods: {
        enviaMensagem: function (e) {
            const _self = this;

            if (_self.mensagem.length > 1) {
                var objMensagem = {
                    texto: _self.mensagem ,
                    remetente: true
                };

                _self.mensagens.push(objMensagem);

                _self.$http.post('/chat', { texto: _self.mensagem }).then(response => {
                    var objResposta = {
                        texto: response.body,
                        remetente: false
                    }
                    _self.mensagens.push(objResposta);

                });

                _self.mensagem = '';
            }
        },
        goToBottom: function () {
            const _self = this;

            _self.$nextTick(function () {
                var container = _self.$el.querySelector(".mensagens-chat");
                container.scrollTop = container.scrollHeight;
            });
        }
    }
});