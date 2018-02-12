#applications!
echo "installing applications.."
apt-get purge wpasupplicant -yqq
apt install hostapd dnsmasq -yqq

echo "configuring access point.."
mv /etc/hostapd/hostapd.conf /etc/hostapd/hostapd.conf.bak
cp hostapd.conf /etc/hostapd/hostapd.conf
echo "you can change the password with 'sudo nano /etc/hostapd/hostapd.conf'"

echo "configuring dhcp.."
mv /etc/dnsmasq.conf /etc/dnsmasq.conf.bak
cp dnsmasq.conf /etc/dnsmasq.conf

echo "starting services.."
ifconfig wlan0 192.168.100.1
dnsmasq
hostapd /etc/hostapd/hostapd.conf &
