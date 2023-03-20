from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gameHome(request):
    return render(request, "home.html")

games = [
    {
        "id": 1,
        "title": "Ultra Fight Da Kyanta 2", 
        "genre": "action", 
        "img": "/static/assets/home/banner.png", 
        "sub": "Ultra Fight Kyanta 2 is a fighting game with a frantic pace and easy to learn controls. You can perform special attacks using single button presses! Fight in 2D battles across various modes using teams of hand-drawn characters.",
        "videoSRC": "/static/assets/videos/videoplayback.mp4"
    },

    {"id": 2, "title": "Doom Eternal", "genre": "rpg", "img": "/static/assets/home/banner2.webp", "sub": "Os exércitos do Inferno invadiram a Terra. Torne-se o Slayer em uma campanha épica para um jogador e derrote demônios entre dimensões para impedir a derradeira destruição da humanidade. A única coisa que eles temem... é você."},
    {"id": 3, "title": "Shadow Warrior", "genre": "strategy", "img": "/static/assets/home/banner3.png", "sub": "Curta uma aventura cheia de adrenalina em um reino mítico japonês na Edição Definitiva de Shadow Warrior 3. Cheia de novos recursos, ela traz para você aproveitar uma mistura ultraviolenta de tiroteio acelerado, combate corpo a corpo afiado e parkour espetacular."},
    {"id": 4, "title": "Mortal Kombat 11", "genre": "strategy", "img": "/static/assets/home/banner4.webp", "sub": "Mortal Kombat está de volta, melhor do que nunca, em uma evolução da icônica franquia."},
    {"id": 5, "title": "Metal Gear Solid V", "genre": "strategy", "img": "/static/assets/home/banner5.png", "sub": "Inaugurando uma nova era para a franquia METAL GEAR com tecnologia de ponta alimentada pelo Fox Engine, METAL GEAR SOLID V: The Phantom Pain irá proporcionar aos jogadores uma experiência de jogo de primeira linha com liberdade tática para realizar missões em mundo aberto."},
    {"id": 6, "title": "Shadow Warrior", "genre": "strategy", "img": "/static/assets/home/banner6.png", "sub": "Curta uma aventura cheia de adrenalina em um reino mítico japonês na Edição Definitiva de Shadow Warrior 3. Cheia de novos recursos, ela traz para você aproveitar uma mistura ultraviolenta de tiroteio acelerado, combate corpo a corpo afiado e parkour espetacular."}
]

def listar_Jogo(request):
    context = {"jogos": games}
    return render(request, "listar_Jogo.html", context)

def detalhe_Jogo(request, id):
    game = games[id - 1]
    return render(request, "detalhe_Jogo.html", {"game": game})
