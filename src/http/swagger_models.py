from flask_restx import fields


def register_models(api):
    success_model = api.model('SuccessResponse', {
        'status': fields.String(example='success'),
        'message': fields.String(example='Operação realizada com sucesso'),
        'data': fields.Raw(description='Conteúdo da resposta')
    })

    error_model = api.model('ErrorResponse', {
        'status': fields.String(example='error'),
        'message': fields.String(example='Mensagem de erro detalhada')
    })

    return success_model, error_model
