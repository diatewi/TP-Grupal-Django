from django.db import models

class Groups(models.Model):
    SERVER_CHOICES = [
        ('LAS', 'LAS'),
        ('BR', 'BR'),
        ('NA', 'NA'),
        ('LAN', 'LAN'),
        ('EUW', 'EUW'),
        ('KR', 'KR'),
        ('EUNE', 'EUNE                         '),
        ('OCE', 'OCE'),
        ('TR', 'TR'),
        ('RU', 'RU'),
        ('JP', 'JP'),
    ]

    GAMEMODE_CHOICES = [
        ('Partida rapida', 'Partida rapida'),
        ('Reclutamiento', 'Reclutamiento'),
        ('Clasificatoria duo', 'Clasificatoria duo'),
        ('Flexible', 'Flexible'),
        ('ARAM', 'ARAM'),
        ('TFT', 'TFT'),
        ('Arena', 'Arena'),
    ]

    server = models.CharField(max_length=25, verbose_name='server', choices=SERVER_CHOICES)
    gamemode = models.CharField(max_length=25, verbose_name='gamemode', choices=GAMEMODE_CHOICES)
    discord = models.CharField(max_length=70, verbose_name='discord', null=True)
    player_name1 = models.CharField(max_length=25, verbose_name='Jugador 1', null=True, blank=True)
    player_name2 = models.CharField(max_length=25, verbose_name='Jugador 2', null=True, blank=True)
    player_name3 = models.CharField(max_length=25, verbose_name='Jugador 3', null=True, blank=True)
    player_name4 = models.CharField(max_length=25, verbose_name='Jugador 4', null=True, blank=True)

    def __str__(self):
        return f"{self.player_name1} | {self.server} | {self.gamemode}"


class FreePlayers(models.Model):
    server = models.CharField(max_length=25, verbose_name='server')
    gamemode = models.CharField(max_length=25, verbose_name='gamemode')
    nickname = models.CharField(max_length=25, verbose_name='nickname')
    discord = models.CharField(max_length=70, verbose_name='discord', null=True)