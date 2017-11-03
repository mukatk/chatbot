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
            _self.mensagem = '';
        }
    }
});