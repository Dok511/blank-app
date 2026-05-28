import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="منصة المزاودة لا سيرفر لست دانس المباشرة", page_icon="🔨", layout="centered")

# رابط صورة السلعة
ITEM_IMAGE_URL = "https://cdn.discordapp.com/attachments/1063839574457069661/1509394032168534158/2026-03-07_005051.png?ex=6a19043c&is=6a17b2bc&hm=a0ae2407865a47c008a90030f80e636e5edac5d6e4fc5186f771eb6d666eee3a"

# إنشاء ذاكرة مشتركة حية على السيرفر لجميع المستخدمين
@st.cache_resource
def get_global_db():
    # وضع وقت انتهاء المزاد بعد 5 دقائق (300 ثانية) من الآن
    return {
        "current_price": 5000, 
        "highest_bidder": "لا يوجد مزايد حالياً",
        "end_time": time.time() + 300  # 5 دقائق دقيقة بدقة
    }

# استدعاء الذاكرة المشتركة
db = get_global_db()

st.title("🔨 منصة المزاودة الحية والمباشرة 🚀")
st.write("---")

# عرض الصورة
st.image(ITEM_IMAGE_URL, caption="سياره كورفت C7", use_container_width=True)

# حساب الوقت المتبقي للمزاد لايف
remaining_time = int(db["end_time"] - time.time())

# عرض العداد التنازلي للوقت
if remaining_time > 0:
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    st.warning(f"⏳ **الوقت المتبقي للمزاد:** {minutes} دقائق و {seconds} ثوانٍ")
else:
    st.error("🚨 **انتهى وقت المزاد رسميًا!**")

# عرض الأسعار الحية الحقيقية من السيرفر المشترك
col1, col2 = st.columns(2)
with col1:
    st.info(f"💰 **أعلى سعر حالي:**\n\n ### {db['current_price']} ريال")
with col2:
    st.success(f"👤 **المتصدّر الآن:**\n\n ### {db['highest_bidder']}")

st.write("---")

# منطقة المزاودة (تشتغل فقط إذا كان هناك وقت متبقي)
if remaining_time > 0:
    st.subheader("سجّل سومك المباشر الآن 👇")
    user_name = st.text_input("اسم المزايد الكامل:", placeholder="اكتب اسمك هنا")

    # حساب أقل سومة مسموحة (السعر الحالي +5000$ زيادة)
    min_next_bid = int(db["current_price"]) + 100
    bid_amount = st.number_input("قيمة مزاودتك ($):", min_value=min_next_bid, value=min_next_bid, step=5000)

    if st.button("🚀 اعتمد السومة لايف"):
        if user_name.strip() == "":
            st.error("الرجاء كتابة اسمك أولاً!")
        else:
            # تحديث الذاكرة العالمية للسيرفر فوراً ليراها الجميع
            db["current_price"] = bid_amount
            db["highest_bidder"] = user_name
            st.balloons()
            st.success(f"كفو يا {user_name}! تم تحديث المزاد عند الجميع بقيمة {bid_amount} ريال.")
            time.sleep(1)
            st.rerun()
else:
    # رسالة تظهر للجميع عند انتهاء الـ 5 دقائق وتعلن الفائز
    st.success(f"🎉 **مبروك للفائز بالمزاد:** {db['highest_bidder']} بقيمة {db['current_price']} ريال")

st.write("---")
# 🔄 إعادة تحديث تلقائي للمتصفح كل ثانيتين لتحديث المؤقت والسومات الجديدة لايف عند الكل
time.sleep(2)
st.rerun()
