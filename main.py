import cc_input
import cc_output
import logic

def main() -> None:
    cc_output.show_start_message()
    while True:
        cc_output.show_options_message()
        answer = cc_input.get_answer()
        s = input()
        if answer == "1":
            s_new = logic.atbash(tt=s)
            print(s_new)
        elif answer == "2":
            p_new = logic.cezar(input_data=s)
            print(p_new)
        elif answer == "3":
            g_new = logic.morza(ar=s)
            print(g_new)
        elif answer == "4":
            break
        else:
            cc_output.show_option_error_message()
        cc_output.show_continue_message()
        answer = cc_input.get_answer()
        if answer != "да":
            break
        cc_output.show_finish_message()


if __name__ == '__main__':
    main()
