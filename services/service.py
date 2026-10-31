
class PrediksiService:
    def tentukan_kelulusan(self, ipk: float, sks: int) -> str:
        # Konstanta batas kelulusan
        BATAS_IPK_MINIMAL = 3.0
        BATAS_SKS_MINIMAL = 140

        # Pemeriksaan persyaratan kelulusan
        if ipk >= BATAS_IPK_MINIMAL and sks >= BATAS_SKS_MINIMAL:
            return "Lulus Tepat Waktu"
        else:
            return "Tidak Lulus"
