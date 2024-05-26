from animals import Animal, Predator, Bird, Herbivore
from visitors import Visitor
import time_management
from cells import Cell
import cowsay
import time
import random

class Animal:
    def __init__(self, name, species, age, health, region, gender,ability=None):
        self.name = name
        self.species = species
        self.age = age
        self.health = health
        self.region = region
        self.gender = gender
        self.abilities = ability

class Zoo:
    def __init__(self):
        self.cells = {}
        self.animals = []
        self.visitors = []
        self.envs = ["Savannah","Kutup","Tropikal Orman"]
        self.default_animal_locations = {
            "Aslan": self.generateRandomId(),
            "Penguen": self.generateRandomId(),
            "Kaplan": self.generateRandomId(),
            "Leopar": self.generateRandomId(),
            "Fil": self.generateRandomId()
        }
        self.default_animal_classes = {
            "Aslan": Predator,
            "Penguen": Bird,
            "Kaplan": Predator,
            "Leopar": Predator,
            "Fil": Herbivore
        }
        self.initialize_animals()

     # Bu fonksiyon, başlangıçtaki hayvanları Kafeslere yerleştirir.
    def initialize_animals(self):
        for animal_name, cell_number in self.default_animal_locations.items():
            if cell_number not in self.cells:
                self.cells[cell_number] = Cell(cell_number,random.choice(self.envs))
            animal_class = self.default_animal_classes[animal_name]
            animal = animal_class(animal_name, random.randint(1,15), random.choice(["iyi","kötü"]), random.choice(["erkek","kadın"]))
            self.cells[cell_number].add_animal(animal)
            self.animals.append(animal)

    # Bu fonksiyon, rastgele bir ID üretir.        
    def generateRandomId(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        return ''.join(random.choice(alphabet) for _ in range(5))
    

    # Bu fonksiyon, hayvanat bahçesinin açık olup olmadığını kontrol eder.
    def is_zoo_open(self, current_time):
        return "09:00" <= current_time <= "19:00"

    # Bu fonksiyon, belirtilen Kafes ID'sini ekler.
    def add_cell(self,regoin):
        cellId = self.generateRandomId()
        if cellId not in self.cells:
            self.cells[cellId] = Cell(cellId,regoin)
            print(f"{cellId}'li kafes {regoin} bölgesine başarıyla eklendi")
        else:
            print("Bu Kafes numarası zaten mevcut.")

    # Bu fonksiyon, belirtilen hayvanı belirtilen Kafesye ekler.
    def add_animal_to_cell(self, cell_number, animal):
        if animal in self.animals:
            print("Bu hayvan zaten hayvanat bahçesinde.")
        else:
            if cell_number in self.cells:
                self.cells[cell_number].add_animal(animal)
                self.animals.append(animal)  
                print(f"Hayvan {animal.name} başarıyla Kafesye eklendi.")
            else:
                print("Kafes bulunamadı.")

    # Bu fonksiyon, belirtilen Kafesden belirtilen hayvanı kaldırır.
    def remove_animal_from_cell(self, cell_number, animal_name):
        if cell_number in self.cells:
            self.cells[cell_number].remove_animal(animal_name.title())
            print("Hayvan Kafesden çıkarıldı.")
        else:
            print("Kafes bulunamadı.")

    # Bu fonksiyon, mevcut çevreleri döndürür.        
    def get_available_env(self):
        envs = self.envs
        return envs   
    

    # Bu fonksiyon, belirtilen Kafesyi kaldırır.
    def remove_cell(self, cell_number):
        if cell_number in self.cells:
            del self.cells[cell_number]
            print("Kafes kaldırıldı.")
        else:
            print("Kafes bulunamadı.")

    # Bu fonksiyon, bir ziyaretçi ekler.
    def add_visitor(self):
        print("Ziyaretçi türünü seçin:")
        print("1. Tek")
        print("2. Öğrenci")
        print("3. Öğretmen")
        print("4. Aile")
        print("5. Arkadaşlar")
        visitor_type_choice = input("Seçiminiz: ")
        
        if visitor_type_choice == '1':
            name = input("İsim girin: ").title()
            while True:
                try:
                    age = int(input("Yaş girin: "))
                    break
                except:
                    print("Sence boyle bir yaş var mı ?")

            preferences = input("Tercihleri girin: ")
            self.visitors.append(Visitor(name, age, "Tek", preferences))
            print("Ziyaretçi eklendi.")
        elif visitor_type_choice == '2':
            name = input("İsim girin: ").title()
            while True:
                try:
                    age = int(input("Yaş girin: "))
                    break
                except:
                    print("Sence boyle bir yaş var mı ?")
            preferences = input("Tercihleri girin: ")
            self.visitors.append(Visitor(name, age, "Öğrenci", preferences))
            print("Ziyaretçi eklendi.")
        elif visitor_type_choice == '3':
            name = input("İsim girin: ").title()
            while True:
                try:
                    age = int(input("Yaş girin: "))
                    break
                except:
                    print("Sence boyle bir yaş var mı ?")
            preferences = input("Tercihleri girin: ")
            self.visitors.append(Visitor(name, age, "Öğretmen", preferences))
            print("Ziyaretçi eklendi.")
        elif visitor_type_choice == '4':
            while True:
                    try:
                        num_people = int(input("Birlikte gelen kişi sayısını girin: "))
                        break
                    except:
                        print("Sence boyle bir aded olur mu ?")
                
            for i in range(num_people):
                name = input(f"{i+1}. kişinin adını girin: ")
                while True:
                    try:
                        age = int(input(f"{i+1}. kişinin yaşını girin: "))
                        break
                    except:
                        print("Sence boyle bir yaş var mı ?")
                
                preferences = input(f"{i+1}. kişinin tercihlerini girin: ")
                self.visitors.append(Visitor(name, age, "Aile", preferences))
            print("Ziyaretçiler eklendi.")
        elif visitor_type_choice == '5':
            while True:
                    try:
                        num_people = int(input("Birlikte gelen kişi sayısını girin: "))
                        break
                    except:
                        print("Sence boyle bir aded olur mu ?")
                
            for i in range(num_people):
                name = input(f"{i+1}. kişinin adını girin: ")
                while True:
                    try:
                        age = int(input(f"{i+1}. kişinin yaşını girin: "))
                        break
                    except:
                        print("Sence boyle bir yaş var mı ?")
                preferences = input(f"{i+1}. arkadaşın tercihlerini girin(virgül ile ayırınız \',\'): ")
                self.visitors.append(Visitor(name, age, "Arkadaşlar", preferences.split(",")))
            print("Ziyaretçiler eklendi.")
        else:
            print("Geçersiz seçim.")

    # Bu fonksiyon, belirtilen ziyaretçiyi kaldırır.
    def remove_visitor(self, visitor_name):
        self.visitors = [v for v in self.visitors if v.name != visitor_name]
        print("Ziyaretçi kaldırıldı.")
  
    def get_animals_spec(self):
        return ['vahşi','kuş','otçul']    

    # Bu fonksiyon, belirtilen Kafesdeki hayvanları listeler.
    def list_animals_in_cell(self, cell_number):
        if cell_number in self.cells:
            animals = self.cells[cell_number].animals
            if animals:
                print(f"{cell_number} Id\'li Kafesdeki hayvanlar:")
                for animal in animals:
                    print(f"İsim: {animal.name}, Tür: {animal.species}, Yaş: {animal.age}, Cinsiyet: {animal.gender}, Durum: {animal.health}")
            else:
                print("Bu Kafesde hayvan yok.")
        else:
            print("Kafes bulunamadı.")
    def get_animal_type_in_a_cell(self,cell_number):
          if cell_number in self.cells:
            animals = self.cells[cell_number].animals
            if animals:
                print(f"{cell_number} Id\'li Kafesdeki hayvanlar:")
                for animal in animals:
                   return animal.species
            else:
                print("Bu Kafesde hayvan yok.")
          else:
            print("Kafes bulunamadı.")   

    # Bu fonksiyon, tüm Kafesleri listeler.
    def list_all_cells(self):
        return list(self.cells)

    # Bu fonksiyon, tüm hayvanları listeler.
    def list_all_animals_in_zoo(self):
        return [animal.name for animal in self.animals]
    

    def get_all_animals_class_in_zoo(self):
        return self.animals

    # Bu fonksiyon, belirtilen hayvanla etkileşimde bulunur.
    def interact_with_animal(self, animal_name):
        print(f"{animal_name} ile etkileşimde bulunuluyor...")

    def handle_different_interactions(self,animal):
        print("1. Hayvanla oyna")
        print("2. Hayvanı besle.")
        print("3. Hayvanı gözlemle")

        interaction_type = input("Seçiminiz: ")
        if interaction_type == '1':
            if animal.species.lower() == "vahşi":
                print("vahşi hayvanlarla oynamak risklidir ! lütfen farklı bir hayvan seçiniz.")
            else:
                self.play_with_animals(animal.name)
        elif interaction_type == '2':
            if animal.species.lower() == "vahşi":
                print("vahşi hayvanlarla beslemek risklidir ! lütfen farklı bir hayvan seçiniz.")
            else:
                self.feed_animals(animal.name)
        elif interaction_type == '3':
           self.observe_animals(animalName=animal.name)
        else:
            print("Geçersiz seçim.")    

    # Bu fonksiyon, hayvanları gözlemleme işlemi yapar.
    def observe_animals(self,animalName):
        print(f"{animalName} Hayvanı gözlemliyorsunuz...")

    # Bu fonksiyon, hayvanlarla oynama işlemi yapar.
    def play_with_animals(self,animalName):
        print(f"{animalName} Hayvanla oynuyorsunuz...")

    # Bu fonksiyon, hayvanları besleme işlemi yapar.
    def feed_animals(self,animalName):
        print(f"{animalName} Hayvanı besliyorsunuz...")

    # Bu fonksiyon, bütün kafesleri yazdırı.    
    def printAllCells(self):
        for i,kafes in enumerate(self.list_all_cells()):
                print(f"{i+1}. Kafes ID: {kafes}, bulunduğu bölge: {self.cells[kafes].region}")    

    # Bu fonksiyon, belirtilen hayvanın bilgilerini günceller.
    def update_animal_info(self, animal_name):
        found = False
        for animal in self.animals:
            if animal.name == animal_name:
                found = True
                print(f"{animal_name} isimli hayvanın bilgileri güncelleniyor:")
                new_age = input("Yeni yaş girin: ")
                new_health = input("Yeni sağlık durumu girin (iyi veya kötü): ")
                animal.age = new_age
                animal.health = new_health
                print("Hayvan bilgileri başarıyla güncellendi.")
                break
        if not found:
            print(f"{animal_name} isimli hayvan hayvanat bahçesinde bulunamadı.")
    def add_region(self,name):
        return self.envs.append(name)      

    # Bu fonksiyon, tüm ziyaretçileri gösterir.
    def show_all_visitors(self):
        print("Ziyaretçi listesi:")
        for visitor in self.visitors:
            print(f"İsim: {visitor.name}, Yaş: {visitor.age}, Tür: {visitor.visitor_type}, Tercihler: {visitor.animal_list}")

# Bu fonksiyon, ana menüyü gösterir ve kullanıcıdan giriş alır.
def main_menu(zoo,current_time):
  
        while True:
            cowsay.cow("HAYVANAT BAHÇESİNE HOŞ GELDİNİZ")
            print(f"Current time: {current_time}\n")
            print("\nBir işlem seçin:\n")
            print("1.  Kafes ekle                                6.  Kafesden hayvan çıkar")
            print("2.  Kafese hayvan ekle                        7.  Kafesi kaldır")
            print("3.  Ziyaretçi ekle                            8.  Ziyaretçiyi kaldır")
            print("4.  Kafesdeki hayvanları listele              9.  Hayvanat bahçesindeki tüm hayvanları listele")
            print("5.  Tüm Kafesleri listele                     10. Hayvanla etkileşimde bulun")
            print("11. Ziyaretçi listesini göster                12. Hayvan bilgilerini güncelle")
            print("13. Yeni bir bölge ekle                       13. Hayvanat bahçesinden çık\n")
            
            choice = input("Seçiminiz: ")

            if choice == "1":
                regions = zoo.envs
                for i in regions:
                    print(i)
                while True:
                    region = input("Bölgenin adını giriniz: ").title()
                    if len(region) < 1:
                        print("Adsız bir bölge ? Çok garip !!")
                    elif region not in regions:
                        print("Sence böyle bir bölge yukarıda yazıyor mu ?")
                    else:
                        break
                zoo.add_cell(region)
            elif choice == "2":
                abilities = []
                print("Mevcut Kafesler: ")
                zoo.printAllCells()
                cell_number = input("Kafes ID\'sini girin: ")
                aType = zoo.get_animal_type_in_a_cell(cell_number)
                animal_name = input("Hayvanın ismini girin: ").title()
                animal_spec_list =  zoo.get_animals_spec()
                for i in animal_spec_list:
                    print(i,end=", ") 
                print()
                while True:
                    animal_species = input("Hayvanın türünü girin: ").lower()
                    if len(animal_species) < 1:
                        print("Adsız bir tür ? Çok garip !!")
                    elif animal_species not in animal_spec_list:
                        print("Sence böyle bir tür yukarıda yazıyor mu ?")    
                    else:
                        break
                if aType.lower() == "vahşi" and animal_species == "vahşi":
                    print(f"vahşi hayvanlar aynı kafesta yaşayamazlar. lütfen yeni bir kafes oluşturun.")      
                    continue 
                elif aType.lower() == "vahşi" and animal_species != "vahşi" :
                    print(f"vahşi hayvanlar ile başka tür hayvan aynı kafeste konulamaz. lütfen yeni bir kafes oluşturun.")        
                    continue
                while True:
                    try:
                        animal_age = int(input("Hayvanın yaşını girin: "))
                        break
                    except:
                        print("Hiç bir zaman yaş sembol olmamıştır ):")   
                while True:
                    animal_health = input("Hayvanın sağlık durumu (iyi veya kötü): ").lower()
                    if len(animal_health) < 1:
                        print("Adsız bir sağlık durumu ? Çok garip !!")
                    elif animal_health not in ["iyi","kötü"]:
                        print("Sence böyle bir sağlık durumu yukarıda yazıyor mu ?")
                    else:
                        break 
                while True:
                    animal_gender = input("Hayvanın cinsiyeti (erkek, dişi): ").lower()
                    if len(animal_gender) < 1:
                        print("Adsız bir cinsiyet ? Çok garip !!")
                    elif animal_gender not in ["erkek","dişi"]:
                        print("Sence böyle bir cinsiyet olur mu? yukarıda yazıyor mu ?")
                    else:
                        break
                while True:
                    try:
                        num_of_abilities = int(input("Kaç hayvan özelliği eklmek istiyorsunuz ? "))
                        break
                    except:
                        print("Sence boyle bir aded olur mu ?")
                for i in range(num_of_abilities):
                    ability = input(f"{i+1}. Özelliği ekleyin: ")
                    abilities.append(ability)
                if animal_species == "vahşi":
                    animal = Predator(animal_name, animal_age, animal_health, animal_gender,abilities)
                elif animal_species == "kuş":
                    animal = Bird(animal_name, animal_age, animal_health, animal_gender,abilities)
                elif animal_species == "Otçul":
                    animal = Herbivore(animal_name, animal_age, animal_health, animal_gender,abilities)
                else:
                    print("Geçersiz hayvan türü.") 
                    continue
                zoo.add_animal_to_cell(cell_number, animal)
            elif choice == "3":
                zoo.add_visitor()
            elif choice == "4":
                zoo.printAllCells()
                cell_number = input("Kafes ID'sini girin: ")
                zoo.list_animals_in_cell(cell_number)
            elif choice == "5":
                cells = zoo.list_all_cells()
                print("Tüm Kafesler:")
                for i,cell in enumerate(cells):
                    print(f"{i}. {cell}")
            elif choice == "6":
                zoo.printAllCells()
                cells = zoo.cells.keys()
                while True:
                    cell_id = input("Kafes ID'sini girin: ")
                    if len(cell_id) < 1:
                        print("Adsız bir bölge ? Çok garip !!")
                    elif cell_id not in cells:
                        print("Yukarıdaki ID'lere bakar mısın ?") 
                    else:
                        break
                zoo.list_animals_in_cell(cell_id)
                animals = [animal.name.lower() for animal in zoo.cells[cell_id].animals]
                while True:
                    animal_name = input("Hayvanın ismini girin: ").lower()
                    if len(animal_name) < 1:
                        print("Adsız bir bölge ? Çok garip !!")
                    elif animal_name not in animals:
                        print("Yukarıdaki hayvanlara bakar mısın ?") 
                    else:
                        break 
                zoo.remove_animal_from_cell(cell_id, animal_name)
            elif choice == "7":
                zoo.printAllCells()
                cell_id = input("Kafes ID'sini girin: ")
                zoo.remove_cell(cell_id)
            elif choice == "8":
                if len(zoo.visitors) <1:
                    print("Ziyaretçi adedi sıfırdır!!")
                else:
                    for i,visitor in enumerate(zoo.visitors):
                        print(f"{i}. {visitor}")
                    visitor_name = input("Ziyaretçinin ismini girin: ")
                    zoo.remove_visitor(visitor_name)
            elif choice == "9":
                animals = zoo.list_all_animals_in_zoo()
                print("Hayvanat bahçesindeki tüm hayvanlar:")
                for i,animal in enumerate(animals):
                    print(f"{i+1}. {animal}")
            elif choice == "10":
                animals = {animal.name: animal for animal in zoo.get_all_animals_class_in_zoo()}
                for animal_name in animals.keys():
                    print(animal_name)
                while True:
                    animal_name = input("Hayvanın ismini girin: ").title()
                    if len(animal_name) < 1:
                        print("Adsız bir hayvan ? Çok garip !!")
                    elif animal_name not in animals:
                        print("Yukarıdaki hayvanlara bakar mısın ?") 
                    else:
                        break
                zoo.handle_different_interactions(animals[animal_name])
            elif choice == "11":
                animals = [name.lower() for name in zoo.list_all_animals_in_zoo()]
                for i,animal in enumerate(zoo.list_all_animals_in_zoo()):
                    print(f"{i+1}. {animal}")
                while True:
                    animal_name = input("Bilgilerini güncellemek istediğiniz hayvanın ismini girin: ").lower()
                    if len(animal_name) < 1:
                        print("Adsız bir hayvan ? Çok garip !!")
                    elif animal_name not in animals:
                        print("Yukarıdaki hayvanlara bakar mısın ?") 
                    else:
                        break
                zoo.update_animal_info(animal_name.title())
            elif choice == "12":
                if len(zoo.visitors) < 1:
                    print("Ziyaretçi yoktur !")
                else:
                    zoo.show_all_visitors()
            elif choice == "13":
                while True:
                    region_name = input("Bölgenin adını giriniz").lower()
                    if len(region_name) < 1:
                        print("Adsız bir bölge ? Çok garip !!")
                    else:
                        break
                zoo.add_region(region_name)  
            elif choice == "14":
                print("Hayvanat bahçesinden çıkılıyor...")
                break    
            else:
                print("Geçersiz seçim, lütfen tekrar deneyin.")

            input("\nDevam etmek için Enter'a basin...")
       
        
def main():
    zoo = Zoo()
    start_time = time.time()
    time_management_instance = time_management.TimeManagement()
    current_time = time_management_instance.generate_random_clock()
 
    while True:
        if zoo.is_zoo_open(current_time):
            main_menu(zoo,current_time)
            repeat = input("Menüyü açmak için herhangi bir tuşa basin veya çikmak için 'kapat' yazin: ")
            if repeat.lower() == 'kapat':
                break
        else:
            print(f"Maalesef sanal hayvanat bahçesi kapalıdır ); ")
            print(f"saat : {current_time}")
            print("çalışma saatleri : her gün 09.00 - 19.00 arası")
            print("10 saniye sonra ugulamadan çıkılacaktır...") 

            for i in range(10, 0, -1):
                print(f"{i}...")
                time.sleep(1)
            break
                

if __name__ == "__main__":
    main()
