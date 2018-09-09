import portScanner as ps

def main():
    """
    主函数
    """
    scanner = ps.PortScanner(target_ports=50)
    
    host_name = 'www.baidu.com'
    message = 'hello'
    scanner.set_thread_limit(1500)

    scanner.set_delay(10)

    scanner.show_target_ports()

    scanner.show_top_k_ports(100)

    output = scanner.scan(host_name,message)

if __name__ == '__main__':
    main()