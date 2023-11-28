import streamlit as st

st.set_page_config(
    page_title="Invesment Advisor",
    page_icon="💵"
)
menu = st.sidebar.selectbox("Menu",("Home","How To Invest","How To Use"))
st.markdown(
    """
    <style>
        .centered-title {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Menampilkan title di tengah
st.markdown("<h1 class='centered-title'> 📈 Invesment Advisor 📈</h1>  ", unsafe_allow_html=True)
if menu == "Home":
    def home_page ():
        st.header("Kenapa ada Invesment Advisor ?")
        st.write("Alasan utama Invesment Advisor ini ada, yaitu demi Nilai AlPRO kelompok kami..")
        st.header("Apa saja yang dapat dilakukan Invesment Advisor ?")
        st.write(""" Invesment Advisor di buat untuk membantu generasi muda dalam memahami dunia investasi.
        """)
        st.write(""" """)
        st.header("WARNING ❗❗❗")
        st.write("Investasi adalah hal yang beresiko  ")
    home_page()
if menu == "How To Invest" :
    def how_to_use():
        st.header("Cara Menggunakan Investasi")
        st.markdown('''Menggunakan investasi melibatkan beberapa langkah penting. Berikut adalah panduan umum tentang cara menggunakan investasi:

                \n - Tentukan Tujuan Investasi:
                \nIdentifikasi tujuan finansial Anda. Apakah itu untuk dana pensiun, pendidikan anak, atau pertumbuhan kekayaan jangka panjang? Mengetahui tujuan akan membantu Anda menentukan strategi investasi yang sesuai.
                \n - Kenali Profil Risiko dan Toleransi Risiko:
                \nTentukan seberapa besar risiko yang bersedia Anda ambil. Profil risiko dan toleransi risiko Anda akan memengaruhi jenis investasi yang paling sesuai untuk Anda, apakah itu saham, obligasi, atau instrumen investasi lainnya.
                \n - Pahami Jenis Investasi:
                \nPelajari berbagai jenis investasi seperti saham, obligasi, reksa dana, properti, dan lainnya. Pahami karakteristik masing-masing jenis investasi, termasuk potensi keuntungan dan risiko.
                \n - Buat Portofolio Investasi yang Diversifikasi:
                \nDiversifikasi dapat membantu mengurangi risiko. Sebaiknya jangan meletakkan semua dana investasi Anda pada satu jenis aset atau satu sektor. Sebaliknya, alokasikan dana Anda di berbagai jenis investasi.
                \n - Riset dan Analisis:
                \nLakukan riset tentang perusahaan atau instrumen investasi yang Anda pertimbangkan. Pelajari kinerja historis, prospek masa depan, dan faktor-faktor yang dapat memengaruhi investasi tersebut.
                \n - Buat Rencana Keuangan:
                \nSusun rencana keuangan yang mencakup strategi investasi Anda. Tetapkan target keuangan, tenggat waktu, dan rencana darurat.
                \n - Pilih Pialang atau Platform Investasi:
                \nJika Anda tidak memiliki pengalaman langsung dalam investasi, pertimbangkan untuk menggunakan jasa pialang atau platform investasi. Pilih pialang atau platform yang dapat memberikan akses ke berbagai instrumen investasi dan menyediakan alat analisis yang berguna.
                \n - Monitor dan Evaluasi:
                \nPantau secara teratur kinerja portofolio investasi Anda. Sesuaikan portofolio jika ada perubahan dalam tujuan keuangan, profil risiko, atau kondisi pasar.
                \n - Reinvestasi Keuntungan:
                \nPertimbangkan untuk reinvestasi keuntungan yang Anda peroleh. Reinvestasi dapat meningkatkan potensi pertumbuhan portofolio Anda.
                \n - Tetap Disiplin dan Sabar:
                \nInvestasi memerlukan disiplin dan kesabaran. Jangan tergoda untuk melakukan keputusan investasi berdasarkan emosi atau perubahan pasar yang jangka pendek.
                    
                \nIngatlah bahwa investasi selalu melibatkan risiko, dan hasil masa lalu tidak menjamin hasil di masa depan. Oleh karena itu, penting untuk terus memperbarui pengetahuan Anda tentang pasar keuangan dan tetap beradaptasi dengan perubahan kondisi ekonomi. Jika Anda merasa kesulitan atau tidak yakin, pertimbangkan untuk berkonsultasi dengan seorang penasihat keuangan profesional.''')
    how_to_use()