class ExpertSystem:
    def __init__(self):
        # Basis pengetahuan: penyakit dan gejala terkait
        self.knowledge_base = {
            "flu": ["demam", "batuk", "nyeri otot", "sakit kepala", "kelelahan"],
            "migren": ["sakit kepala", "mual", "sensitif terhadap cahaya"],
            "keracunan makanan": ["mual", "diare", "nyeri perut"],
            "depresi": ["kelelahan", "kecemasan", "perubahan nafsu makan"],
            "diabetes": ["sering haus", "sering buang air kecil", "kelelahan"],
            "covid-19": ["demam", "batuk", "sesak napas", "kehilangan indra penciuman"]
        }

    def get_symptoms(self, disease):
        # Mengembalikan gejala berdasarkan penyakit
        return self.knowledge_base.get(disease.lower(), None)

def main():
    print("Selamat datang di Sistem Pakar Gejala Penyakit")
    print("Masukkan nama penyakit yang ingin Anda ketahui gejalanya (ketik 'selesai' untuk mengakhiri):")

    while True:
        disease = input("Penyakit: ").strip().lower()
        if disease == 'selesai':
            break

        # Membuat instance dari sistem pakar
        expert_system = ExpertSystem()
        symptoms = expert_system.get_symptoms(disease)

        if symptoms:
            print(f"Gejala yang terkait dengan penyakit '{disease}':")
            for symptom in symptoms:
                print(f"- {symptom}")
        else:
            print(f"Tidak ada informasi gejala untuk penyakit '{disease}'.")

if __name__ == "__main__":
    main()