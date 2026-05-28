import streamlit as st
import requests
import json
import time

# إعدادات الصفحة
st.set_page_config(page_title="منصة لاست دانس المزاودة ", page_icon="🔨", layout="centered")

# رابط السيرفر السحابي المشترك (رابط وهمي مخصص لمزادك لجعل البيانات لايف وموحدة للجميع)
# ملاحظة: يمكنك تغيير الرقم 8518 لأي رقم سري خاص بك لضمان خصوصية مزادك
DB_URL = "https://api.keyvalue.xyz/7c3b2e5a/salman_auction_2026"
ITEM_IMAGE_URL = "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&q=80&w=1000"

# دالة لجلب البيانات الحية من السيرفر للجميع
def get_live_data():
    try:
        response = requests.get(DB_URL)
        if response.status_code == 200:
            return json.loads(response.text)
    except:
        pass
    # إذا كانت أول مرة والموقع فاضي، يرجع البيانات الابتدائية (5000 ريال)
    return {"item_name": "السلعة المميزة", "current_price": 5000, "highest_bidder": "لا يوجد مزايد حالياً"}

# دالة لحفظ المزاودة الجديدة في السيرفر السحابي فوراً
def save_live_data(price, bidder):
    data = {"item_name": "السلعة المميزة", "current_price": price, "highest_bidder": bidder}
    try:
        requests.post(DB_URL, data=json.dumps(data))
    except:
        st.error("عذراً، حدث خطأ في الاتصال بالسيرفر المباشر!")

# جلب البيانات الحالية الحية
live_data = get_live_data()

st.title("🔨 منصة المزاودة الحية والمباشرة 🚀")
st.write("هذه الصفحة تُحدّث لايف، وأي شخص يزاود يظهر اسمه وسعره عند الجميع فوراً!")
st.write("---")

# عرض الصورة
st.image(ITEM_IMAGE_URL, caption="صورة السلعة المعروضة", use_container_width=True)

# عرض الأسعار الحية الحقيقية القادمة من السيرفر للكل
col1, col2 = st.columns(2)
with col1:
    st.info(f"💰 **أعلى سعر حالي:**\n\n ### {live_data['current_price']} ريال")
with col2:
    st.success(f"👤 **المتصدّر الآن:**\n\n ### {live_data['highest_bidder']}")

st.write("---")

# منطقة المزاودة
st.subheader("سجّل سومك المباشر الآن 👇")
user_name = st.text_input("اسم المزايد الكامل:", placeholder="اكتب اسمك هنا")

# حساب أقل سومة مسموحة (السعر الحالي + 100 ريال زيادة)
min_next_bid = int(live_data['current_price']) + 5000

bid_amount = st.number_input("قيمة مزاودتك (ريال):", min_value=min_next_bid, value=min_next_bid, step=5000)

if st.button("🚀 اعتمد السومة لايف"):
    if user_name.strip() == "":
        st.error("الرجاء كتابة اسمك أولاً!")
    else:
        # حفظ البيانات في السيرفر السحابي فوراً ليراها الجميع
        save_live_data(bid_amount, user_name)
        st.balloons()
        st.success(f"كفو يا {user_name}! تم تحديث المزاد عالمياً بقيمة {bid_amount} ريال.")
        time.sleep(1)
        st.rerun()

# زر التحديث اليدوي الفوري
if st.button("🔄 تحديث ورؤية السومات الجديدة"):
    st.rerun()
