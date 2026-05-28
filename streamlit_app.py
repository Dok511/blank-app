import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="منصة لاست دانس للمزاودة", page_icon="🔨", layout="centered")

# رابط صورة السلعة
ITEM_IMAGE_URL = "https://cdn.discordapp.com/attachments/1063839574457069661/1509394032168534158/2026-03-07_005051.png?ex=6a19043c&is=6a17b2bc&hm=a0ae2407865a47c008a90030f80e636e5edac5d6e4fc5186f771eb6d666eee3a"

# الاتصال بقاعدة بيانات Streamlit المباشرة للجميع
conn = st.connection("local_db", type="dict")

# جلب البيانات الحية أو وضع بيانات ابتدائية لو كانت أول مرة
if "current_price" not in conn:
    conn["current_price"] = 5000
    conn["highest_bidder"] = "لا يوجد مزايد حالياً"

st.title("🔨 منصة لاست دانس للمزاودة  🚀")
st.write("هذه الصفحة تُحدّث تلقائياً كل ثانيتين، وأي شخص يزاود يظهر سعره عند الجميع فوراً!")
st.write("---")

# عرض الصورة
st.image(ITEM_IMAGE_URL, caption="صورة السلعة كورفت س 7", use_container_width=True)

# عرض الأسعار الحية الحقيقية القادمة من السيرفر للكل
col1, col2 = st.columns(2)
with col1:
    st.info(f"💰 **أعلى سعر حالي:**\n\n ### {conn['current_price']} ريال")
with col2:
    st.success(f"👤 **المتصدّر الآن:**\n\n ### {conn['highest_bidder']}")

st.write("---")

# منطقة المزاودة
st.subheader("سجّل سومك المباشر الآن 👇")
user_name = st.text_input("اسم المزايد الكامل:", placeholder="اكتب اسمك هنا")

# حساب أقل سومة مسموحة (السعر الحالي + 100 ريال زيادة)
min_next_bid = int(conn["current_price"]) + 5000

bid_amount = st.number_input("قيمة مزاودتك (ريال):", min_value=min_next_bid, value=min_next_bid, step=5000)

if st.button("🚀 اعتمد السومة لايف"):
    if user_name.strip() == "":
        st.error("الرجاء كتابة اسمك أولاً!")
    else:
        # حفظ البيانات في السيرفر السحابي فوراً ليراها الجميع
        conn["current_price"] = bid_amount
        conn["highest_bidder"] = user_name
        st.balloons()
        st.success(f"كفو يا {user_name}! تم تحديث المزاد عند الجميع بقيمة {bid_amount} ريال.")
        time.sleep(1)
        st.rerun()

st.write("---")
# 🔄 كود التحديث التلقائي الذكي (يجبر الصفحة تتحدث كل ثانيتين بدون تدخل منك)
time.sleep(2)
st.rerun()
