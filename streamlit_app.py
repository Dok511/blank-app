import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="المزاد مغلق", page_icon="🔒", layout="centered")

# --- اكتب بيانات الفائز الحقيقي هنا ---
FINAL_PRICE = 6400  # السعر النهائي اللي وقف عنده المزاد
WINNER_NAME = "سلمان"  # اسم الشخص اللي فاز بالسلعة

# تنسيق الصفحة لجعل القفل والكتابة في المنتصف بشكل كبير
st.markdown("""
    <style>
    .closed-container {
        text-align: center;
        padding: 40px;
    }
    .lock-icon {
        font-size: 100px;
        margin-bottom: 10px;
    }
    .main-title {
        font-size: 45px;
        color: #FF4B4B;
        font-weight: bold;
    }
    .winner-box {
        background-color: #1E1E1E;
        border: 2px solid #262626;
        padding: 30px;
        border-radius: 15px;
        margin-top: 30px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    }
    </style>
""", unsafe_allow_html=True)

# عرض القفل الكبير وكلمة المزاد مغلق في المنتصف
st.markdown(f"""
    <div class="closed-container">
        <div class="lock-icon">🔒</div>
        <div class="main-title">المزاد مغلق حالياً</div>
        <p style="color: #888888; font-size: 18px;">تم انتهاء وقت المزاودة رسميًا وإغلاق المنصة.</p>
        
        <div class="winner-box">
            <h2 style="color: #00E676; margin-bottom: 15px;">🎉 مبروك للفائز النهائي 🎉</h2>
            <h3 style="color: #FFFFFF; font-size: 28px; margin: 10px 0;">👤 المشتري: {WINNER_NAME}</h3>
            <h3 style="color: #00E676; font-size: 32px; margin: 10px 0;">💰 القيمة: {FINAL_PRICE} ريال</h3>
        </div>
        
        <p style="margin-top: 40px; color: #555555; font-size: 14px;">شكرًا لجميع المشاركين على الحماس والدعم.</p>
    </div>
""", unsafe_allow_html=True)
