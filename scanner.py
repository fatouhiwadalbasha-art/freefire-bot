import socket

# تحديد الهدف (يمكنك كتابة IP لجهازك أو موقع للتجربة القانونية)
target = "127.0.0.1" 

# قائمة بالمنافذ الشهيرة التي نريد فحصها
ports = [21, 22, 80, 443]

print(f"جاري فحص الهدف: {target}...")

for port in ports:
    # إنشاء اتصال شبكي عبر بروتوكول TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0) # تحديد وقت الانتظار بثانية واحدة
    
    # محاولة الاتصال بالمنفذ
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f" [+] المنفذ {port} مفتوح (Open)")
    else:
        print(f" [-] المنفذ {port} مغلق (Closed)")
        
    s.close()
