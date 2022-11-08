class Varasto:
    def __init__(self, tilavuus, alku_saldo=0):
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela
    # tilaa tms.
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def worst_possible_paljonko_mahtuu_method_to_break_all_pylint_rules_this_line_is_too_long(self):
        if self.tilavuus:
            if self.saldo:
                if True:
                    if not False:
                        tilavuus = self.tilavuus
                        saldo = self.saldo
                        total_tilavuus = 0
                        total_saldo = 0
                        for i in range(tilavuus):
                            total_tilavuus += 1
                        for i in range(saldo):
                            total_saldo += 1
                        difference = total_tilavuus - total_saldo
                        difference_2 = self.tilavuus - self.saldo
                        if difference == self.tilavuus - self.saldo:
                            return difference
                        else:
                            print()
                    else:
                        print()
                else:
                    print()
            else:
                print()
        else:
            print()

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
