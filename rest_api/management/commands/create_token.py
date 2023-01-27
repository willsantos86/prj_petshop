from django.core.management.base import BaseCommand,Token, User

class Command(BaseCommand):
    help = 'Cria um novo token para ser usado'

    def add_arguments(self, parser):
        parser.add_argument('--usarname',required=True)
        parser.add_argument('--password',required=True)

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        self.stdout.write(
            self.style.WARNING(f'Criando usuário com o {username}')
        )
        user = User(username=username)
        user.first_name = username,
        user.set_password(password)
        user.save()
        self.stdout.write(
            self.style.SUCCESS('fUsuário Criado')
        )
        self.stdout.write(
            self.style.WARNING(f'Criando token para usuário')
        )
        token = Token.objects.create(user=user)
        self.stdout.write(
            self.style.SUCCESS(f'Token criando para o usuário: {token.key}')
        )