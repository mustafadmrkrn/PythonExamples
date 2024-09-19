class Cezeri(CezeriParent):    
    def __init__(self, id = 0):
        super().__init__(id = id, keyboard = False, sensor_mode = DUZELTILMIS)

        self.baslangic_bolgesi = self.harita.bolge(self.gnss.enlem, self.gnss.boylam)
        self.hedef_enlem = self.hedefler[0].bolge.enlem
        self.hedef_boylam = self.hedefler[0].bolge.boylam
        self.donus_threshold = 45 # derece cinsinden
        self.hedef_threshold = 5 # ne cinsinden ben de bilmiyorum
        self.inis_hiz_threshold = 20 # yere x metre kaldığında yavaşla (lidar verisi)
        self.hedef_hiz_threshold = 20 # hedefe x metre kaldığında yavaşla (gnss verisi)
        self.hedef_no = 0 # dokumayın

    def rotate(self,cx,cy,x,y,angle):
        radians = math.radians(angle)
        cos = math.cos(radians)
        sin = math.sin(radians)
        nx = (cos * (x-cx) + (sin * (y-cy))) + cx
        ny = (cos * (y-cy) - (sin * (x-cx))) + cy
        return nx, ny
    
    def calculate_distance(self, p1, p2):
        x1,y1 = p1
        x2,y2 = p2
        return math.sqrt((x2-x1)**2+(y2-y1)**2)

    def run(self):
        #print("Manyetometre:", self.manyetometre)
        #print("Lidar:", self.lidar)
        #print("Radar:", self.radar)
        #print("IMU:", self.imu)
        #print("Barometre:", self.barometre)
        #print("Batarya:", self.batarya)
        #print("Motor:", self.motor)

        current_enlem = self.gnss.enlem
        current_boylam = self.gnss.boylam
        current_yukseklik = self.barometre.irtifa

        distance = self.calculate_distance((current_enlem, current_boylam), (self.hedef_enlem, self.hedef_boylam))
        current_rotation = -math.degrees(self.manyetometre.veri)

        rotated_x, rotated_y = self.rotate(cx = current_enlem, cy = current_boylam, x = self.hedef_enlem, y = self.hedef_boylam, angle = -current_rotation)
        
        #print(f"Rotated X: {rotated_x}, Rotated Y: {rotated_y}")
        
        turn_radian = math.atan2(rotated_y - current_boylam, rotated_x - current_enlem)
        turn_angle = math.degrees(turn_radian)
        
        print(f"Turn Angle: {turn_angle}")
        #print(f"current Konum: Enlem: {current_enlem}, Boylam: {current_boylam}")
        #print(f"Hedef Konum: Enlem: {self.hedef_enlem}, Boylam: {self.hedef_boylam}")
        #print(f"Diff Enlem: {diff_enlem}, Diff Boylam: {diff_boylam}")
        

        #120 + 100 < 1 & 120 + 110 > -1

        if distance > self.hedef_threshold:
            self.yukari_git(HIZLI)
            if current_yukseklik < 90:
                print(f"current_yukseklik: {current_yukseklik}")
                return
            self.dur()

            self.don(turn_radian)
            
            if turn_angle < self.donus_threshold and turn_angle > -self.donus_threshold:
                print("donus tamamlandi")

                if distance < self.hedef_hiz_threshold:
                    self.ileri_git(YAVAS)
                else:
                    self.ileri_git(HIZLI)
        elif self.hedefler[self.hedef_no].amac == INIS:
            print("hedefe varildi")
            self.dur()
            if self.lidar.hata:
                if self.radar.mesafe > self.inis_hiz_threshold:
                    self.asagi_git(HIZLI)
                else:
                    self.asagi_git(YAVAS)
            else:
                if self.lidar.mesafe > self.inis_hiz_threshold:
                    self.asagi_git(HIZLI)
                else:
                    self.asagi_git(YAVAS)
        elif self.hedefler[self.hedef_no].amac == ZIYARET:
            self.hedef_no = self.hedef_no + 1
            self.hedef_enlem = self.hedefler[0].bolge.enlem
            self.hedef_boylam = self.hedefler[0].bolge.boylam



cezeri_1 = Cezeri(id = 1)
cezeri_2 = Cezeri(id = 2)
while robot.is_ok():
    (cezeri_1.run())
    robot.is_ok()
    (cezeri_2.run())
    #print(cezeri_1.hedefler[cezeri_1.hedef_no].sira)
    #print("test")
    #for i, hedef in enumerate(cezeri_2.hedefler):
    #    print(hedef, i)
    #print(cezeri_2.gnss.enlem)
    #print(cezeri_2.gnss.boylam)