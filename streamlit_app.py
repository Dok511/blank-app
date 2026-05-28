import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="المزاد مغلق", page_icon="🔒", layout="centered")

# تنسيق الصفحة لجعل القفل والكتابة في المنتصف بشكل كبير وبدون زوائد
st.markdown("""
    <style>
    .closed-container {
        text-align: center;
        padding: 60px 20px;
    }
    .lock-icon {
        font-size: 120px;
        margin-bottom: 20px;
    }
    .main-title {
        font-size: 45px;
        color: #FF4B4B;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .sub-title {
        color: #888888;
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# عرض القفل والكلام فقط في المنتصف
st.markdown("""
    <div class="closed-container">
        <div class="lock-icon">🔒</div>
        <div class="main-title">المزاد مغلق حالياً</div>
        <div class="sub-title">LD1 تم انتهاء وقت المزاودة رسميًا واختصار الدسكورد .</div>
    </div>
""", unsafe_allow_html=True)
