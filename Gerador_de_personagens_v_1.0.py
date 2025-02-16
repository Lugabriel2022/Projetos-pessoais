from tkinter import *
from tkinter import ttk
from random import *
import os

jan = Tk()
class Funcs():
    def listas(self):
        lista_classes = ['Feiticeiro', 'Mago', 'Artifice', 'Alquimista', 'Guerreiro', 'Paladino', 'Cavaleiro', 'Ladino',
                         'Arqueiro']
        lista_mage = ['Feiticeiro', 'Mago', 'Artifice']
        lista_raças = ['Humano', 'Elfo', 'Anão', 'Kobolt', 'Catfolk', 'Gigante', 'Dragão', 'Kitsune', 'Long']
        lista_cores = ['Azul', 'Verde', 'Branco', 'Preto', 'Roxo', 'Violeta', 'Vermelho', 'Castanho', 'Cinza',
                       'Dourado']
        lista_cor_pele = ['Palida', 'Clara', 'Pardo', 'Escura', 'Negra']
        lista_chifres = ['Sheep', 'Bode', 'Addax', 'Saiga', 'Deer']
        lista_fisicos = ['magro', 'esguio', 'musculoso', 'robusto']
        lista_tipos_cabelo = ['liso', 'cacheado', 'Ondulado', 'Crespo']
        lista_cabelos = ['muito longo', 'longo', 'curto', 'muito curto', 'raspado']
        lista_sobrenome = ['Gojo', 'Kisuke', 'Souza', 'Dragonheart', 'Moonlight', 'Torres', 'Draco', 'Madelin',
                           'Masamune', 'Urokitake']
        lista_elementos = ['Ar', 'Agua', 'Fogo', 'Terra', 'Luz', 'Escuridão', 'Sagrado', 'Demoniaco']
        lista_seios = ['A', 'B', 'C', 'D', 'E', 'F']
        lista_origem = ['Nobre', 'Aprendiz de Mago', 'Orfão']
        lista_corpo = ['Bestial', 'Humanoide']
        lista_natureza = ['Holy', 'Demon', 'Fluid', 'Digital', 'Fire', 'Eletric', 'Mecanico']
        lista_assets = ['Arms', 'Wings', 'Tail', 'Legs']
        lista_mod = ['Multi', 'Taur', 'Modular', 'Naga', 'Wheleed']
        lista_nomem = ['Lucas', 'Satoru', 'Kaio', 'Toriko', 'Jimmy', 'Minosuke', 'Mauricio', 'Edward']
        lista_nomef = ['Luna', 'Satory', 'Ciel', 'Myra', 'Saphira', 'Karina', 'Mary', 'Lumi']
        lista_titulo = ['Heroi', 'Prodigio', 'Divindade']

        return (lista_classes, lista_mage, lista_raças, lista_cores, lista_cor_pele, lista_chifres, lista_fisicos,
                lista_tipos_cabelo, lista_cabelos, lista_sobrenome, lista_elementos, lista_seios, lista_origem,
                lista_corpo, lista_natureza, lista_assets, lista_mod, lista_nomem, lista_nomef, lista_titulo)

    def sorteios(self):
        listas = self.listas()
        (lista_classes, lista_mage, lista_raças, lista_cores, lista_cor_pele, lista_chifres, lista_fisicos,
         lista_tipos_cabelo, lista_cabelos, lista_sobrenome, lista_elementos, lista_seios, lista_origem, lista_corpo,
         lista_natureza, lista_assets, lista_mod, lista_nomem, lista_nomef, lista_titulo) = listas
        classe = choice(lista_classes)
        raça = choice(lista_raças)
        cor_cabelo = choice(lista_cores)
        cor_olhos = choice(lista_cores)
        cor_pele = choice(lista_cor_pele)
        cor_escamas = choice(lista_cores)
        tipo_corpo = choice(lista_corpo)
        fisico = choice(lista_fisicos)
        cabelo = choice(lista_cabelos)
        busto = choice(lista_seios)
        origem = choice(lista_origem)
        natureza = choice(lista_natureza)
        lista_natureza.remove(natureza)
        sobrenome = choice(lista_sobrenome)
        mutação = choice(lista_mod)
        asset = choice(lista_assets)
        chifres = choice(lista_chifres)
        titulo = choice(lista_titulo)
        nomef = choice(lista_nomef)
        nomem = choice(lista_nomem)
        En = choice(lista_elementos)
        lista_elementos.remove(En)
        em = choice(lista_elementos)
        lista_elementos.remove(em)
        em2 = choice(lista_elementos)
        lista_elementos.remove(em2)
        em3 = choice(lista_elementos)

        return (classe, raça, cor_cabelo, cor_olhos, cor_pele, cor_escamas, tipo_corpo, fisico, cabelo, busto, origem, natureza, sobrenome, mutação, asset,
                chifres, titulo, nomef, nomem, En, em, em2, em3)

    def Raça(self):
        (classe, raça, cor_cabelo, cor_olhos, cor_pele, cor_escamas, tipo_corpo, fisico, cabelo, busto, origem, natureza,
        sobrenome, mutação, asset, chifres, titulo, nomef, nomem, En, em, em2, em3) = self.sorteios()
        Id = 0
        altm = ''
        altcm = ''
        idade = ''
        raça1 = raça
        fisico1 = fisico
        # estatisticas
        Força = randint(10, 50)
        Constituição = randint(10, 50)
        Agilidade = randint(10, 50)
        Resistencia = randint(10, 50)
        Inteligencia = randint(10, 50)
        Sabedoria = randint(10, 50)
        Percepção = randint(10, 50)
        Arcano = randint(10, 50)
        Sorte = randint(10, 100)
        Carisma = randint(10, 50)
        # Aleatoriedade controlada
        if fisico1 == 'Musculoso':
            Força = randint(30, 50)

        elif fisico1 == 'Esquio':
            Força = randint(10, 30)
            Agilidade = randint(30, 50)

        elif fisico1 == 'Robusto':
            Constituição == randint(30, 50)
            Resistencia == randint(30, 50)

        #if ch2 == 'n':
        #    mutação = 'Null'
        # Caracteristicas raciais
        if raça1 == 'Anão':
            altm = 1
            altcm = randint(00, 50)
            idade = randint(40, 500)
            Constituição += 20
            Resistencia += 15
            Id = 1

        elif raça1 == 'Humano':
            altm = randint(1, 2)
            altcm = randint(00, 99)
            idade = randint(8, 22)
            Constituição += 15
            Id = 2

        elif raça1 == 'Elfo':
            altm = randint(1, 2)
            altcm = randint(00, 99)
            idade = randint(100, 1000)
            Arcano += 15
            Carisma += 10
            Sabedoria += 20
            Id = 3

        elif raça1 == 'Catfolk':
            altm = randint(1, 2)
            altcm = randint(00, 99)
            idade = randint(8, 22)
            Agilidade += 15
            Sorte += 10
            Percepção += 20
            Id = 4

        elif raça1 == 'Kobolt':
            altm = 1
            altcm = randint(00, 30)
            idade = randint(8, 500)
            Força += 15
            Arcano += 10
            Percepção += 10
            Id = 5

        elif raça1 == 'Gigante':
            altm = randint(5, 8)
            altcm = randint(00, 99)
            idade = randint(8, 32)
            Força += 25
            Constituição += 20
            Resistencia += 20
            Id = 6

        elif raça1 == 'Kitsune':
            altm = randint(1, 4)
            altcm = randint(00, 99)
            idade = randint(100, 1000)
            Inteligencia += 30
            Arcano += 25
            Constituição += 20
            Agilidade += 15
            Percepção += 15
            Sabedoria += 15
            Carisma += 40
            Id = 7

        elif raça1 in ['Dragão', 'Long']:
            altm = randint(10, 35)
            altcm = randint(00, 99)
            idade = randint(500, 100000)
            Força = randint(200, 50000)
            Constituição = randint(2000, 50000)
            Agilidade = randint(2000, 50000)
            Resistencia = randint(2000, 50000)
            Inteligencia = randint(2000, 50000)
            Sabedoria = randint(2000, 50000)
            Percepção = randint(2000, 50000)
            Arcano = randint(2000, 50000)
            Sorte = randint(1000, 10000)
            Carisma = randint(2000, 50000)
            Id = 8


        return (Força, Agilidade, Resistencia, Carisma, Sorte, Arcano, Percepção, Sabedoria, Inteligencia, altm, altcm, idade, Constituição, Id, raça1, fisico1)

    def Limpar(self):
        self.tx_nome.config(state = NORMAL)
        self.tx_gen.config(state = NORMAL)
        self.tx_idade.config(state = NORMAL)
        self.tx_fc.config(state = NORMAL)
        self.tx_busto.config(state= NORMAL)
        self.tx_corp.config(state = NORMAL)
        self.tx_raca.config(state = NORMAL)
        self.tx_alt.config(state=NORMAL)
        self.tx_cab.config(state=NORMAL)
        self.tx_for.config(state=NORMAL)
        self.tx_cons.config(state=NORMAL)
        self.tx_agi.config(state=NORMAL)
        self.tx_res.config(state=NORMAL)
        self.tx_int.config(state=NORMAL)
        self.tx_sab.config(state=NORMAL)
        self.tx_per.config(state=NORMAL)
        self.tx_arc.config(state=NORMAL)
        self.tx_sor.config(state=NORMAL)
        self.tx_car.config(state=NORMAL)
        self.tx_tcab.config(state=NORMAL)
        self.tx_escamas.config(state=NORMAL)
        self.tx_chifres.config(state=NORMAL)
        self.tx_em.config(state=NORMAL)
        self.tx_em2.config(state=NORMAL)
        self.tx_em3.config(state=NORMAL)
        self.tx_en.config(state=NORMAL)
        self.tx_classe.config(state=NORMAL)
        self.tx_coro.config(state=NORMAL)
        self.tx_tcorp.config(state=NORMAL)
        # ========================================================================
        self.tx_for.delete(1.0, END)
        self.tx_cons.delete(1.0, END)
        self.tx_agi.delete(1.0, END)
        self.tx_res.delete(1.0, END)
        self.tx_int.delete(1.0, END)
        self.tx_sab.delete(1.0, END)
        self.tx_per.delete(1.0, END)
        self.tx_arc.delete(1.0, END)
        self.tx_sor.delete(1.0, END)
        self.tx_car.delete(1.0, END)
        self.tx_cab.delete(1.0, END)
        self.tx_tcab.delete(1.0, END)
        self.tx_alt.delete(1.0, END)
        self.tx_raca.delete(1.0, END)
        self.tx_corp.delete(1.0, END)
        self.tx_busto.delete(1.0, END)
        self.tx_fc.delete(1.0, END)
        self.tx_gen.delete(1.0, END)
        self.tx_nome.delete(1.0, END)
        self.tx_idade.delete(1.0, END)
        self.tx_escamas.delete(1.0, END)
        self.tx_chifres.delete(1.0, END)
        self.tx_em.delete(1.0, END)
        self.tx_em2.delete(1.0, END)
        self.tx_em3.delete(1.0, END)
        self.tx_en.delete(1.0, END)
        self.tx_classe.delete(1.0, END)
        self.tx_coro.delete(1.0, END)
        self.tx_tcorp.delete(1.0, END)
        # ========================================================================
        self.tx_nome.config(state = DISABLED)
        self.tx_gen.config(state = DISABLED)
        self.tx_idade.config(state = DISABLED)
        self.tx_fc.config(state = DISABLED)
        self.tx_busto.config(state = DISABLED)
        self.tx_corp.config(state = DISABLED)
        self.tx_raca.config(state = DISABLED)
        self.tx_alt.config(state = DISABLED)
        self.tx_cab.config(state = DISABLED)
        self.tx_tcab.config(state = DISABLED)
        self.tx_for.config(state=DISABLED)
        self.tx_cons.config(state=DISABLED)
        self.tx_agi.config(state=DISABLED)
        self.tx_res.config(state=DISABLED)
        self.tx_int.config(state=DISABLED)
        self.tx_sab.config(state=DISABLED)
        self.tx_per.config(state=DISABLED)
        self.tx_arc.config(state=DISABLED)
        self.tx_sor.config(state=DISABLED)
        self.tx_car.config(state=DISABLED)
        self.tx_escamas.config(state=DISABLED)
        self.tx_chifres.config(state=DISABLED)
        self.tx_em.config(state=DISABLED)
        self.tx_em2.config(state=DISABLED)
        self.tx_em3.config(state=DISABLED)
        self.tx_en.config(state=DISABLED)
        self.tx_classe.config(state=DISABLED)
        self.tx_coro.config(state=DISABLED)
        self.tx_tcorp.config(state=DISABLED)
        self.var_g.set('')

    def Gerar(self):
        (classe, raça, cor_cabelo, cor_olhos, cor_pele, cor_escamas, tipo_corpo, fisico, cabelo, busto, origem, natureza,
        sobrenome, mutação, asset, chifres, titulo, nomef, nomem, En, em, em2, em3) = self.sorteios()

        (Força, Agilidade, Resistencia, Carisma, Sorte, Arcano, Percepção, Sabedoria, Inteligencia, altm, altcm, idade, Constituição, Id, raça1, fisico1) = self.Raça()

        (lista_classes, lista_mage, lista_raças, lista_cores, lista_cor_pele, lista_chifres, lista_fisicos,
         lista_tipos_cabelo, lista_cabelos, lista_sobrenome, lista_elementos, lista_seios, lista_origem,
         lista_corpo, lista_natureza, lista_assets, lista_mod, lista_nomem, lista_nomef, lista_titulo) = self.listas()
        if self.var_g.get() in ('M', 'F'):
            self.tx_idade.config(state = NORMAL)
            self.tx_fc.config(state = NORMAL)
            self.tx_busto.config(state = NORMAL)
            self.tx_corp.config(state = NORMAL)
            self.tx_raca.config(state = NORMAL)
            self.tx_alt.config(state=NORMAL)
            self.tx_cab.config(state=NORMAL)
            self.tx_tcab.config(state=NORMAL)
            self.tx_for.config(state=NORMAL)
            self.tx_cons.config(state=NORMAL)
            self.tx_agi.config(state=NORMAL)
            self.tx_res.config(state=NORMAL)
            self.tx_int.config(state=NORMAL)
            self.tx_sab.config(state=NORMAL)
            self.tx_per.config(state=NORMAL)
            self.tx_arc.config(state=NORMAL)
            self.tx_sor.config(state=NORMAL)
            self.tx_car.config(state=NORMAL)
            self.tx_em.config(state=NORMAL)
            self.tx_em2.config(state=NORMAL)
            self.tx_em3.config(state=NORMAL)
            self.tx_en.config(state=NORMAL)
            self.tx_classe.config(state=NORMAL)
            self.tx_escamas.config(state=NORMAL)
            self.tx_nome.config(state=NORMAL)
            self.tx_gen.config(state=NORMAL)
            self.tx_chifres.config(state=NORMAL)
            self.tx_coro.config(state=NORMAL)
            self.tx_tcorp.config(state=NORMAL)
            #=============================================================
            self.tx_tcab.delete(1.0, END)
            self.tx_cab.delete(1.0, END)
            self.tx_gen.delete(1.0, END)
            self.tx_nome.delete(1.0, END)
            self.tx_idade.delete(1.0, END)
            self.tx_fc.delete(1.0, END)
            self.tx_busto.delete(1.0, END)
            self.tx_corp.delete(1.0, END)
            self.tx_raca.delete(1.0, END)
            self.tx_alt.delete(1.0, END)
            self.tx_escamas.delete(1.0, END)
            self.tx_for.delete(1.0, END)
            self.tx_cons.delete(1.0, END)
            self.tx_agi.delete(1.0, END)
            self.tx_res.delete(1.0, END)
            self.tx_int.delete(1.0, END)
            self.tx_sab.delete(1.0, END)
            self.tx_per.delete(1.0, END)
            self.tx_arc.delete(1.0, END)
            self.tx_sor.delete(1.0, END)
            self.tx_car.delete(1.0, END)
            self.tx_chifres.delete(1.0, END)
            self.tx_em.delete(1.0, END)
            self.tx_em2.delete(1.0, END)
            self.tx_em3.delete(1.0, END)
            self.tx_en.delete(1.0, END)
            self.tx_classe.delete(1.0, END)
            self.tx_coro.delete(1.0, END)
            self.tx_tcorp.delete(1.0, END)
            #===================================================================================
            self.tx_for.insert(INSERT, Força)
            self.tx_cons.insert(INSERT, Constituição)
            self.tx_agi.insert(INSERT, Agilidade)
            self.tx_res.insert(INSERT, Resistencia)
            self.tx_int.insert(INSERT, Inteligencia)
            self.tx_sab.insert(INSERT, Sabedoria)
            self.tx_per.insert(INSERT, Percepção)
            if classe in lista_mage or raça1 in ['Dragão', 'Long', 'Kobolt', 'Kitsune']:
                self.tx_arc.insert(INSERT, Arcano)
            self.tx_sor.insert(INSERT, Sorte)
            self.tx_car.insert(INSERT, Carisma)
            if self.var_g.get() == 'M':
                self.tx_nome.insert(INSERT, f'{nomem} {sobrenome}')
                self.tx_gen.insert(INSERT, 'Masculino')
                self.tx_busto.insert(INSERT, '')
            elif self.var_g.get() == 'F':
                self.tx_nome.insert(INSERT, f'{nomef} {sobrenome}')
                self.tx_gen.insert(INSERT, 'Feminino')
                self.tx_busto.insert(INSERT, busto)
                if raça1 in ['Dragão', 'Long', 'Kitsune'] and tipo_corpo == 'Bestial':
                    self.tx_busto.delete(1.0, END)
                    self.tx_busto.insert(INSERT, '')
            self.tx_idade.insert(INSERT, idade)
            self.tx_fc.insert(INSERT, fisico1)
            if raça1 in ['Dragão', 'Long', 'Kobolt']:
                self.tx_escamas.insert(INSERT, cor_escamas)
                self.tx_chifres.insert(INSERT, chifres)
                self.tx_en.insert(INSERT, En)
            else:
                self.tx_corp.insert(INSERT, cor_pele)
            self.tx_raca.insert(INSERT, raça1)
            self.tx_alt.insert(INSERT, f'{altm}, {altcm} m')
            self.tx_cab.insert(INSERT, cor_cabelo)
            self.tx_tcab.insert(INSERT, cabelo)
            self.tx_classe.insert(INSERT, classe)
            if classe in lista_mage or raça1 in ['Dragão', 'Long', 'Kitsune']:
                self.tx_em.insert(INSERT, em)
                if Arcano >= 35:
                    self.tx_em2.insert(INSERT, em2)
                if Arcano >= 50:
                    self.tx_em3.insert(INSERT, em3)
            self.tx_coro.insert(INSERT, cor_olhos)
            if raça1 in ['Dragão', 'Long', 'Kitsune']:
                self.tx_tcorp.insert(INSERT, tipo_corpo)
            else:
                self.tx_tcorp.insert(INSERT, '')
            # ==================================================================================
            self.tx_nome.config(state = DISABLED)
            self.tx_gen.config(state = DISABLED)
            self.tx_idade.config(state = DISABLED)
            self.tx_fc.config(state = DISABLED)
            self.tx_busto.config(state = DISABLED)
            self.tx_corp.config(state = DISABLED)
            self.tx_alt.config(state=DISABLED)
            self.tx_cab.config(state = DISABLED)
            self.tx_tcab.config(state = DISABLED)
            self.tx_for.config(state=DISABLED)
            self.tx_cons.config(state=DISABLED)
            self.tx_agi.config(state=DISABLED)
            self.tx_res.config(state=DISABLED)
            self.tx_int.config(state=DISABLED)
            self.tx_sab.config(state=DISABLED)
            self.tx_per.config(state=DISABLED)
            self.tx_arc.config(state=DISABLED)
            self.tx_sor.config(state=DISABLED)
            self.tx_car.config(state=DISABLED)
            self.tx_escamas.config(state=DISABLED)
            self.tx_chifres.config(state=DISABLED)
            self.tx_em.config(state=DISABLED)
            self.tx_em2.config(state=DISABLED)
            self.tx_em3.config(state=DISABLED)
            self.tx_en.config(state=DISABLED)
            self.tx_classe.config(state=DISABLED)
            self.tx_coro.config(state=DISABLED)
            self.tx_tcorp.config(state=DISABLED)
            self.tx_raca.config(state=DISABLED)
            self.ficha()


    def ficha(self):

        nome1 = self.tx_nome.get(1.0, END).strip()
        idade = self.tx_idade.get(1.0, END).strip()
        fisico1 = self.tx_fc.get(1.0, END).strip()
        busto1 = self.tx_busto.get(1.0, END).strip()
        cor_pele1 = self.tx_corp.get(1.0, END).strip()
        alt = self.tx_alt.get(1.0, END).strip()
        cor_cabelo1 = self.tx_cab.get(1.0, END).strip()
        cabelo1 = self.tx_tcab.get(1.0, END).strip()
        Força = self.tx_for.get(1.0, END).strip()
        Constituição = self.tx_cons.get(1.0, END).strip()
        Agilidade = self.tx_agi.get(1.0, END).strip()
        Resistencia = self.tx_res.get(1.0, END).strip()
        Inteligencia = self.tx_int.get(1.0, END).strip()
        Sabedoria = self.tx_sab.get(1.0, END).strip()
        Percepção = self.tx_per.get(1.0, END).strip()
        Arcano = int(self.tx_arc.get(1.0, END))
        Sorte = self.tx_sor.get(1.0, END).strip()
        Carisma = self.tx_car.get(1.0, END).strip()
        cor_escamas1 = self.tx_escamas.get(1.0, END).strip()
        chifres1 = self.tx_chifres.get(1.0, END).strip()
        em1 = self.tx_em.get(1.0, END).strip()
        em21 = self.tx_em2.get(1.0, END).strip()
        em31 = self.tx_em3.get(1.0, END).strip()
        En1 = self.tx_en.get(1.0, END).strip()
        classe1 = self.tx_classe.get(1.0, END).strip()
        cor_olhos1 = self.tx_coro.get(1.0, END).strip()
        tipo_corpo1 = self.tx_tcorp.get(1.0, END).strip()
        raça1 = self.tx_raca.get(1.0, END).strip()

        ficha_txt = []
        if self.var_g.get() == 'F':
            ficha_txt.append(f'Nome: {nome1}')
            ficha_txt.append('Genero: Feminino')
        if self.var_g.get() == 'M':
            ficha_txt.append(f'Nome: {nome1}')
            ficha_txt.append('Genero: Masculino')
        ficha_txt.append(f'Idade: {idade} anos')
        ficha_txt.append(f'Raça: {raça1}')
        ficha_txt.append(f'Altura: {alt}')
        if raça1 in ['Humano', 'Elfo', 'Gigante', 'Catfolk', 'Gigante', 'Anão']:
            ficha_txt.append(f'Cor da pele: {cor_pele1}')
        # if mod == True:
        # ficha_txt.append(f'Mutação: {mutação1}')
        # ficha_txt.append(f'Natureza: {natureza1}')
        # if mutação == 'Multi':
        # ficha_txt.append(f'Caracteristica mutada: {num} {asset}')
        if raça1 in ['Dragão', 'Kobolt', 'Long']:
            ficha_txt.append(f'Cor escamas: {cor_escamas1}')
            ficha_txt.append(f'Chifres : {chifres1}')
        if raça1 in ['Dragão', 'Long']:
            ficha_txt.append(f'Corpo: {tipo_corpo1}')
            ficha_txt.append(f'Elemento Natural: {En1}')
            if tipo_corpo1 == 'Humanoide':
                ficha_txt.append(f'Busto: {busto1}')
        if self.var_g.get() == 'F' and raça1 in ['Humano', 'Elfo', 'Kobolt', 'Gigante', 'Catfolk', 'Gigante',
                                                 'Kitsune', 'Anão']:
            ficha_txt.append(f'Busto: {busto1}')
        ficha_txt.append(f'Cor do olhos: {cor_olhos1}')
        if self.var_g.get() == 'F' and raça1 in ['Humano', 'Elfo', 'Gigante', 'Catfolk', 'Gigante', 'Kitsune',
                                                 'Anão']:
            ficha_txt.append(f'Cor do Cabelo: {cor_cabelo1}')
            ficha_txt.append(f'Tipo de cabelo: {cabelo1}')
        ficha_txt.append(f'Fisico: {fisico1}')
        ficha_txt.append(f'Classe: {classe1}')
        #ficha_txt.append(f'Titulo: {titulo1}')
        #ficha_txt.append(f'Origem: {origem1}')
        ficha_txt.append('Stats' + '-' * 20 + '|')
        if classe1 in ['Mago', 'Feiticeiro', 'Artifice'] or raça1 in ['Dragão', 'Long', 'Kitsune']:
            ficha_txt.append(f'Arcano: {int(Arcano)}')
            ficha_txt.append(f'1ºElemento magico: {em1}')
            if Arcano >= 35:
                ficha_txt.append(f'2ºElemento magico: {em21}')
                if Arcano >= 50:
                    ficha_txt.append(f'3ºElemento magico: {em31}')
        ficha_txt.append(f'Força: {int(Força)}')
        ficha_txt.append(f'Resistencia: {int(Resistencia)}')
        ficha_txt.append(f'Agilidade: {int(Agilidade)}')
        ficha_txt.append(f'Constituição: {int(Constituição)}')
        ficha_txt.append(f'Inteligencia: {int(Inteligencia)}')
        ficha_txt.append(f'Sabedoria: {int(Sabedoria)}')
        ficha_txt.append(f'Percepção: {int(Percepção)}')
        ficha_txt.append(f'Carisma: {int(Carisma)}')
        ficha_txt.append(f'Sorte: {int(Sorte)}')

#        for linha in ficha_txt:
#           print(linha)

        return ficha_txt

    def salvar(self, ficha_txt, arquivo='Save.txt'):
        modo = 'a' if os.path.exists(arquivo) else 'w'
        with open(arquivo, modo) as file:
            for linha in ficha_txt:
                file.write(linha + '\n')
            file.write('\n')
            file.write('-' * 30 + '\n')
            file.write('\n')

    def salvar_personagem(self):
        ficha_txt = self.ficha()
        self.salvar(ficha_txt)
        print('Persongem salvo com sucesso')


class Application(Funcs):
    def __init__(self):
        self.jan = jan
        self.var_g = StringVar()
        self.tela()
        self.frames()
        self.widgets_frame_1()
        self.widgets_frame_2()
        self.widgets_frame_3()
        self.widgets_frame_4()
        jan.mainloop()

    def tela(self):
        jan.title('Gerador de personagens')
        jan.geometry('700x500')
        jan.resizable(True, True)
        jan.maxsize(width = 1020, height = 960)
        jan.minsize(width = 600, height = 400)

    def frames(self):
        self.frame_1 = Frame(self.jan, bg = 'lightgray')
        self.frame_1.place(relx = 0.01, rely = 0.01, relwidth = 0.2, relheight = 0.6)
        self.frame_2 = Frame(self.jan, bg = 'lightgray')
        self.frame_2.place(relx = 0.22, rely = 0.01, relwidth = 0.5, relheight = 0.8)
        self.frame_3 = Frame(self.jan, bg = 'lightgray')
        self.frame_3.place(relx = 0.73, rely = 0.01, relwidth = 0.26, relheight = 0.6)
        self.frame_4 = Frame(self.jan, bg= 'lightgray')
        self.frame_4.place(relx= 0.73, rely= 0.62, relwidth = 0.26, relheight = 0.37)

    def widgets_frame_1(self):
        #botão save
        self.bt_save = ttk.Button(self.frame_1, text = 'Save', command=self.salvar_personagem)
        self.bt_save.place(relx = 0.02, rely = 0.01, relwidth = 0.5, relheight = 0.1)
        #botão novo
        self.bt_novo = ttk.Button(self.frame_1, text = 'Novo', command = self.Limpar)
        self.bt_novo.place(relx = 0.02, rely = 0.12, relwidth = 0.5, relheight = 0.1)
        #botão gerar
        self.bt_gerar = ttk.Button(self.frame_1, text = 'Gerar', command = self.Gerar)
        self.bt_gerar.place(relx = 0.02, rely = 0.23, relwidth = 0.5, relheight = 0.1)
        #label sexo
        self.lb_sexo = Label(self.frame_1, text = 'Escolha o Genero', bg= 'lightgray')
        self.lb_sexo.place(relx = 0.02, rely = 0.34)
        #checkbox sexo
        self.rd_sexo_1 = ttk.Radiobutton(self.frame_1, text = 'Masculino', variable = self.var_g , value = 'M')
        self.rd_sexo_1.place(relx = 0.02, rely = 0.43)
        self.rd_sexo_2 = ttk.Radiobutton(self.frame_1, text='Feminino', variable = self.var_g, value = 'F')
        self.rd_sexo_2.place(relx=0.02, rely=0.54)

    def widgets_frame_2(self):
        x = 0.22
        self.lb_nome = Label(self.frame_2, text = 'Nome: ', bg = 'lightgray')
        self.lb_nome.place(relx = 0.01, rely = 0.02)
        self.lb_sexo = Label(self.frame_2, text = 'Genero: ', bg = 'lightgray')
        self.lb_sexo.place(relx = 0.01, rely = 0.08)
        self.lb_idade = Label(self.frame_2, text = 'Idade:', bg = 'lightgray')
        self.lb_idade.place(relx = 0.01, rely = 0.14)
        self.lb_fc = Label(self.frame_2, text = 'Fisico:', bg = 'lightgray')
        self.lb_fc.place(relx = 0.01, rely = 0.2)
        self.lb_busto = Label(self.frame_2, text = 'Busto:', bg = 'lightgray')
        self.lb_busto.place(relx = 0.01, rely = 0.26)
        self.lb_corp = Label(self.frame_2, text = 'Cor pele:', bg = 'lightgray')
        self.lb_corp.place(relx =0.01, rely = 0.32)
        self.lb_raca = Label(self.frame_2, text = 'Raça:', bg = 'lightgray')
        self.lb_raca.place(relx = 0.01, rely = 0.38)
        self.lb_alt = Label(self.frame_2, text = 'Altura:', bg = 'lightgray')
        self.lb_alt.place(relx = 0.01, rely = 0.44)
        self.lb_cab = Label(self.frame_2, text='Cor Cabelo:', bg='lightgray')
        self.lb_cab.place(relx=0.01, rely=0.50)
        self.lb_tcab = Label(self.frame_2, text='Tipo Cabelo:', bg='lightgray')
        self.lb_tcab.place(relx=0.01, rely=0.56)
        self.lb_escamas = Label(self.frame_2, text = "Cor escamas:", bg= 'lightgray')
        self.lb_escamas.place(relx = 0.01, rely = 0.62)
        self.lb_chifres = Label(self.frame_2, text = 'Chifres:', bg= 'lightgray')
        self.lb_chifres.place(relx = 0.01, rely = 0.68)
        self.lb_coro = Label(self.frame_2, text ='Cor Olhos:', bg= 'lightgray')
        self.lb_coro.place(relx = 0.01, rely = 0.74)
        self.lb_tcorp = Label(self.frame_2, text= 'Tipo Corpo:', bg= 'lightgray')
        self.lb_tcorp.place(relx = 0.01, rely = 0.80)
        #text
        self.tx_nome = Text(self.frame_2, wrap=WORD)
        self.tx_nome.place(relx=x, rely=0.02, relwidth=0.7, relheight=0.05)
        self.tx_gen = Text(self.frame_2, wrap=WORD)
        self.tx_gen.place(relx=x, rely=0.08, relwidth=0.3, relheight=0.05)
        self.tx_idade = Text(self.frame_2, wrap=WORD)
        self.tx_idade.place(relx=x, rely=0.14, relwidth=0.13, relheight=0.05)
        self.tx_fc = Text(self.frame_2, wrap=WORD)
        self.tx_fc.place(relx=x, rely=0.2, relwidth=0.25, relheight=0.05)
        self.tx_busto = Text(self.frame_2, wrap=WORD)
        self.tx_busto.place(relx=x, rely=0.26, relwidth=0.05, relheight=0.05)
        self.tx_corp = Text(self.frame_2, wrap=WORD)
        self.tx_corp.place(relx=x, rely=0.32, relwidth=0.25, relheight=0.05)
        self.tx_raca = Text(self.frame_2, wrap=WORD)
        self.tx_raca.place(relx=x, rely=0.38, relwidth=0.25, relheight=0.05)
        self.tx_alt = Text(self.frame_2, wrap=WORD)
        self.tx_alt.place(relx=x, rely=0.44, relwidth=0.25, relheight=0.05)
        self.tx_cab = Text(self.frame_2, wrap=WORD)
        self.tx_cab.place(relx=x, rely=0.50, relwidth=0.25, relheight=0.05)
        self.tx_tcab = Text(self.frame_2, wrap=WORD)
        self.tx_tcab.place(relx=x, rely=0.56, relwidth=0.35, relheight=0.05)
        self.tx_escamas = Text(self.frame_2, wrap=WORD)
        self.tx_escamas.place(relx=x, rely=0.62, relwidth=0.25, relheight=0.05)
        self.tx_chifres = Text(self.frame_2, wrap=WORD)
        self.tx_chifres.place(relx = x, rely = 0.68, relwidth = 0.25, relheight = 0.05)
        self.tx_coro = Text(self.frame_2, wrap=WORD)
        self.tx_coro.place(relx = x, rely = 0.74, relwidth = 0.25, relheight = 0.05)
        self.tx_tcorp = Text(self.frame_2, wrap=WORD)
        self.tx_tcorp.place(relx= x, rely= 0.8, relwidth = 0.25, relheight = 0.05)

    def widgets_frame_3(self):
        x1 = 0.01
        t1 = 0.36
        t2 = 0.07
        c = 'lightgray'
        self.lb_stats = Label(self.frame_3, text = 'Estatisticas', bg = c)
        self.lb_stats.place(relx = 0.5, rely = 0.04, anchor = 'center')
        #estatisticas
        self.lb_for = Label(self.frame_3, text = 'For:', bg = c)
        self.lb_for.place(relx = x1, rely = 0.06)
        self.tx_for = Text(self.frame_3)
        self.tx_for.place(relx = 0.2, rely = 0.06, relwidth = t1, relheight = t2)
        self.lb_cons = Label(self.frame_3, text = 'Cons:', bg = c)
        self.lb_cons.place(relx = x1, rely = 0.14)
        self.tx_cons = Text(self.frame_3)
        self.tx_cons.place(relx=0.2, rely=0.14, relwidth=t1, relheight=t2)
        self.lb_agi = Label(self.frame_3, text = 'Agi:', bg = c)
        self.lb_agi.place(relx = x1, rely = 0.22)
        self.tx_agi = Text(self.frame_3)
        self.tx_agi.place(relx=0.2, rely=0.22, relwidth=t1, relheight=t2)
        self.lb_res = Label(self.frame_3, text='Res:', bg=c)
        self.lb_res.place(relx=x1, rely=0.3)
        self.tx_res = Text(self.frame_3)
        self.tx_res.place(relx=0.2, rely=0.3, relwidth=t1, relheight=t2)
        self.lb_int = Label(self.frame_3, text='Int:', bg=c)
        self.lb_int.place(relx=x1, rely=0.38)
        self.tx_int = Text(self.frame_3)
        self.tx_int.place(relx=0.2, rely=0.38, relwidth=t1, relheight=t2)
        self.lb_sab = Label(self.frame_3, text='Sab:', bg=c)
        self.lb_sab.place(relx=x1, rely=0.46)
        self.tx_sab = Text(self.frame_3)
        self.tx_sab.place(relx=0.2, rely=0.46, relwidth=t1, relheight=t2)
        self.lb_per = Label(self.frame_3, text='Per:', bg=c)
        self.lb_per.place(relx=x1, rely=0.54)
        self.tx_per = Text(self.frame_3)
        self.tx_per.place(relx=0.2, rely=0.54, relwidth=t1, relheight=t2)
        self.lb_arc = Label(self.frame_3, text='Arc:', bg=c)
        self.lb_arc.place(relx=x1, rely=0.62)
        self.tx_arc = Text(self.frame_3)
        self.tx_arc.place(relx=0.2, rely=0.62, relwidth=t1, relheight=t2)
        self.lb_sor = Label(self.frame_3, text='Sor:', bg=c)
        self.lb_sor.place(relx=x1, rely=0.7)
        self.tx_sor = Text(self.frame_3)
        self.tx_sor.place(relx=0.2, rely=0.7, relwidth=t1, relheight=t2)
        self.lb_car = Label(self.frame_3, text='Car:', bg=c)
        self.lb_car.place(relx=x1, rely=0.78)
        self.tx_car = Text(self.frame_3)
        self.tx_car.place(relx=0.2, rely=0.78, relwidth=t1, relheight=t2)

    def widgets_frame_4(self):
        #labels
        self.lb_magi = Label(self.frame_4, text= 'Caracteristicas magicas', bg= 'lightgray')
        self.lb_magi.place(relx = 0.5, rely = 0.05, anchor= 'center')
        self.lb_classe = Label(self.frame_4, text = 'Classe:', bg= 'lightgray')
        self.lb_classe.place(relx = 0.01, rely = 0.1)
        self.lb_em = Label(self.frame_4, text = 'Elemento 1:', bg= 'lightgray')
        self.lb_em.place(relx = 0.01, rely = 0.2)
        self.lb_em2 = Label(self.frame_4, text = 'Elemento 2:', bg= 'lightgray')
        self.lb_em2.place(relx = 0.01, rely = 0.3)
        self.lb_em3 = Label(self.frame_4, text = 'Elemento 3:', bg = 'lightgray')
        self.lb_em3.place(relx = 0.01, rely = 0.4)
        self.lb_en = Label(self.frame_4, text = 'Elemento Nat:', bg = 'lightgray')
        self.lb_en.place(relx = 0.01, rely = 0.5)
        #Text
        self.tx_classe = Text(self.frame_4, wrap = WORD)
        self.tx_classe.place(relx = 0.45, rely = 0.1, relwidth = 0.5, relheight = 0.1)
        self.tx_em = Text(self.frame_4, wrap = WORD)
        self.tx_em.place(relx = 0.45, rely = 0.2, relwidth = 0.5, relheight = 0.1)
        self.tx_em2 = Text(self.frame_4, wrap = WORD)
        self.tx_em2.place(relx = 0.45, rely = 0.3, relwidth =0.5, relheight = 0.1)
        self.tx_em3 = Text(self.frame_4, wrap = WORD)
        self.tx_em3.place(relx = 0.45, rely = 0.4, relwidth = 0.5, relheight = 0.1)
        self.tx_en = Text(self.frame_4, wrap = WORD)
        self.tx_en.place(relx = 0.45, rely = 0.5, relwidth = 0.5, relheight = 0.1)

Application()