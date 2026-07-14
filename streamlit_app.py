import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="منصة المزاودة لا سيرفر لست دانس المباشرة", page_icon="🔨", layout="wide")

# رابط صورة السلعة
ITEM_IMAGE_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTz_XVRMM0xSwRUAZsPGEGuYX7FAn2oanM3m4Earb13yA&s=10"

# 🛑 القائمة السوداء لحسابات الديسكورد المتبندة 🛑
# اكتب هنا يوزر ديسكورد الشخص اللي تبي تبنده (اكتبه بدقة مثل: salman123)
BANNED_DISCORD_ACCOUNTS = ["banned_user_here", "another_banned_user"] 

# إنشاء ذاكرة مشتركة حية على السيرفر لجميع المستخدمين
@st.cache_resource
def get_global_db():
    return {
        "current_price": 5000, 
        "highest_bidder": "لا يوجد مزايد حالياً",
        "end_time": time.time() + 300,  # 5 دقائق
        "history": []  # قائمة لتخزين سجل المزاودات السابقة
    }

# استدعاء الذاكرة المشتركة
db = get_global_db()

st.title("🔨 منصة المزاودة لا سيرفر لست دانس المباشرة 🚀")
st.write("---")

# حساب الوقت المتبقي للمزاد لايف
remaining_time = int(db["end_time"] - time.time())

# تقسم الشاشة إلى عمودين كبيرين (عمود للسجل وعمود للمزاد)
col_history, col_main = st.columns([1.2, 2])

# ==================== (العمود الأول: سجل المزاودات) ====================
with col_history:
    st.subheader("📜 سجل السومات الحالية")
    if not db["history"]:
        st.info("لا توجد سومات سابقة حتى الآن. كن أول المزاودين!")
    else:
        # عرض السومات مرتبة من الأحدث إلى الأقدم (تشمل الاسم وحساب ديسكورد)
        for bid in reversed(db["history"]):
            st.markdown(f"👤 **{bid['name']}** (`{bid['discord']}`)")
            st.markdown(f"💰 سام بـ **{bid['amount']} $**")
            st.caption(f"⏱️ {bid['time']}")
            st.write("---")

# ==================== (العمود الثاني: المزاد والسلعة) ====================
with col_main:
    # عرض الصورة
    st.image(ITEM_IMAGE_URL, caption="صورة السلعة المعروضة", use_container_width=True)

    # عرض العداد التنازلي للوقت
    if remaining_time > 0:
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        st.warning(f"⏳ **الوقت المتبقي للمزاد:** {minutes} دقائق و {seconds} ثوانٍ")
    else:
        st.error("🚨 **انتهى وقت المزاد رسميًا!**")

    # عرض الأسعار الحية الحقيقية من السيرفر المشترك
    c1, c2 = st.columns(2)
    with c1:
        st.info(f"💰 **أعلى سعر حالي:**\n\n ### {db['current_price']} $")
    with c2:
        st.success(f"👤 **المتصدّر الآن:**\n\n ### {db['highest_bidder']}")

    st.write("---")

    # منطقة المزاودة (تشتغل فقط إذا كان هناك وقت متبقي)
    if remaining_time > 0:
        st.subheader("سجّل سومك المباشر الآن 👇")
        
        # خانات الإدخال الجديدة
        user_name = st.text_input("اسم المزايد الكامل:", placeholder="اكتب اسمك هنا")
        user_discord = st.text_input("حسابك في ديسكورد (Discord Username):", placeholder=": --------")

        # حساب أقل سومة مسموحة (السعر الحالي + 5000 $ زيادة)
        min_next_bid = int(db["current_price"]) + 5000
        bid_amount = st.number_input("قيمة مزاودتك ($):", min_value=min_next_bid, value=min_next_bid, step=5000)

        if st.button("🚀 اعتمد السومة لايف"):
            if user_name.strip() == "" or user_discord.strip() == "":
                st.error("الرجاء كتابة اسمك وحسابك في ديسكورد أولاً!")
            
            # ⛔ التحقق من البند عن طريق الديسكورد ⛔
            elif user_discord.strip().lower() in [account.lower() for account in BANNED_DISCORD_ACCOUNTS]:
                st.error("❌ عذراً، لقد تم حظرك من المشاركة في هذا المزاد!")
                
            else:
                # توقيت السومة الحالي
                current_time_str = time.strftime('%H:%M:%S', time.localtime())
                
                # إضافة السومة الحالية في السجل (تشمل الاسم، السعر، والديسكورد)
                db["history"].append({
                    "name": user_name,
                    "discord": user_discord.strip(),
                    "amount": bid_amount,
                    "time": current_time_str
                })
                
                # تحديث السعر الحالي والممتصدر (يظهر الاسم والديسكورد فوق كمتصدر)
                db["current_price"] = bid_amount
                db["highest_bidder"] = f"{user_name} ({user_discord})"
                
                st.balloons()
                st.success(f"كفو يا {user_name}! تم تحديث المزاد عند الجميع بقيمة {bid_amount} ريال.")
                time.sleep(1)
                st.rerun()
    else:
        # رسالة تظهر للجميع عند انتهاء الـ 5 دقائق وتعلن الفائز
        st.success(f"🎉 **مبروك للفائز بالمزاد:** {db['highest_bidder']} بقيمة {db['current_price']} $")

st.write("---")
# 🔄 إعادة تحديث تلقائي للمتصفح كل ثانيتين لتحديث المؤقت والسومات الجديدة لايف عند الكل
time.sleep(2)
st.rerun()
