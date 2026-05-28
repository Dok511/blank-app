import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="منصة المزاد الحية", page_icon="🔨", layout="centered")

# دالة لقراءة وتخزين البيانات في ذاكرة السيرفر المشتركة لجميع المستخدمين
if 'auction_data' not in st.session_state:
    st.session_state.auction_data = {
        "item_name": "سلعة مميزة (تستطيع تغيير الاسم من الكود)",
        "current_price": 100,  # السعر الابتدائي
        "highest_bidder": "لا أحد حتى الآن",
        "end_time": time.time() + 3600  # وقت انتهاء المزاد (بعد ساعة)
    }

st.title("🔨 منصة المزاودة الحية")
st.write("مرحباً بكم في المزاد! المزاودة تحدّث تلقائياً عند الجميع.")
st.write("---")

# عرض تفاصيل المزاد الحالية في بطاقات ملونة
col1, col2 = st.columns(2)
with col1:
    st.metric(label="💰 أعلى سعر الحالي", value=f"{st.session_state.auction_data['current_price']} ريال")
with col2:
    st.metric(label="👤 صاحب أعلى سعر", value=st.session_state.auction_data['highest_bidder'])

# حساب الوقت المتبقي للمزاد
remaining_time = int(st.session_state.auction_data['end_time'] - time.time())
if remaining_time > 0:
    st.warning(f"⏳ الوقت المتبقي للمزاد: {remaining_time // 60} دقيقة و {remaining_time % 60} ثانية")
else:
    st.error("🚨 انتهى وقت المزاد رسميًا!")

st.write("---")

# منطقة المزاودة
if remaining_time > 0:
    st.subheader("شارك وسجّل مزاودتك الآن 👇")
    
    # إدخال اسم المزايد
    user_name = st.text_input("أدخل اسمك بالكامل:", key="user_name")
    
    # تحديد القيمة (تلقائياً تكون أعلى من السعر الحالي بـ 10 ريال)
    min_next_bid = st.session_state.auction_data['current_price'] + 10
    bid_amount = st.number_input("قيمة مزاودتك (ريال):", min_value=min_next_bid, value=min_next_bid, step=10)
    
    if st.button("🚀 اضغط لاعتماد المزاودة"):
        if user_name.strip() == "":
            st.error("الرجاء كتابة اسمك أولاً لتتمكن من المزاودة!")
        else:
            # تحديث البيانات المشتركة للسيرفر
            st.session_state.auction_data['current_price'] = bid_amount
            st.session_state.auction_data['highest_bidder'] = user_name
            st.success(f"تم تسجيل مزاودتك بنجاح بقيمة {bid_amount} ريال باسم {user_name}!")
            time.sleep(1)
            st.rerun()
else:
    st.success(f"🎉 مبروك للفائز بالمزاد: {st.session_state.auction_data['highest_bidder']} بقيمة {st.session_state.auction_data['current_price']} ريال")

# زر لتحديث الصفحة يدوياً لرؤية آخر الأسعار
if st.button("🔄 تحديث الأسعار"):
    st.rerun()
