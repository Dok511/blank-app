import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="منصة المزاودة الملكية", page_icon="🔨", layout="centered")

# --- بيانات المزاد (تعديل السعر والصورة من هنا) ---
STARTING_PRICE = 5000 # السعر اللي يبدأ منه المزاد
# ضع رابط صورتك هنا (بين علامتي التنصيص)
ITEM_IMAGE_URL = "file:///C:/Users/ALOSTATH/OneDrive/Pictures/Screenshots/%D9%84%D9%82%D8%B7%D8%A9%20%D8%B4%D8%A7%D8%B4%D8%A9%202026-03-07%20005051.png" 

if 'auction_data' not in st.session_state:
    st.session_state.auction_data = {
        "item_name": "السلعة المعروضة (اكتب اسمها هنا)",
        "current_price": STARTING_PRICE,
        "highest_bidder": "لا يوجد مزايد حالياً",
        "end_time": time.time() + 3600  # المزاد ينتهي بعد ساعة
    }

st.title("🔨 منصة المزاودة الحية")
st.write("---")

# --- عرض صورة السلعة ---
st.image(ITEM_IMAGE_URL, caption="صورة السلعة المعروضة للمزاودة", use_container_width=True)

# --- عرض الأسماء والأسعار في بطاقات فخمة ---
col1, col2 = st.columns(2)
with col1:
    st.info(f"💰 **أعلى سعر حالي:**\n\n ### {st.session_state.auction_data['current_price']} ريال")
with col2:
    st.success(f"👤 **المتصدّر الآن:**\n\n ### {st.session_state.auction_data['highest_bidder']}")

# حساب الوقت
remaining_time = int(st.session_state.auction_data['end_time'] - time.time())
if remaining_time > 0:
    st.warning(f"⏳ **الوقت المتبقي:** {remaining_time // 60} دقيقة و {remaining_time % 60} ثانية")
else:
    st.error("🚨 انتهى المزاد!")

st.write("---")

# --- منطقة دخول المزايدين ---
if remaining_time > 0:
    st.subheader("سجّل مزاودتك الآن 👇")
    
    user_name = st.text_input("اسم المزايد:", placeholder="اكتب اسمك الثلاثي")
    
    # أقل مزاودة قادمة (السعر الحالي + 100 ريال كزيادة منطقية)
    min_next_bid = st.session_state.auction_data['current_price'] + 100
    
    bid_amount = st.number_input("قيمة مزاودتك (ريال):", 
                                 min_value=min_next_bid, 
                                 value=min_next_bid, 
                                 step=5000)
    
    if st.button("🚀 اعتمد المزاودة"):
        if user_name.strip() == "":
            st.error("يرجى كتابة الاسم لاعتماد السومة!")
        else:
            st.session_state.auction_data['current_price'] = bid_amount
            st.session_state.auction_state = True # للتحديث
            st.session_state.auction_data['highest_bidder'] = user_name
            st.balloons() # احتفال بسيط عند كل مزاودة
            st.success(f"كفو يا {user_name}! سومتك {bid_amount} هي الأعلى الآن.")
            time.sleep(2)
            st.rerun()

# زر تحديث يدوي
if st.button("🔄 تحديث حالة المزاد"):
    st.rerun()
