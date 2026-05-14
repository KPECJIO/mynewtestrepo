import error_logger
import Input_handler, output_handler, eval_expression


def main():
    while True:
        try:
            a, b, action = Input_handler.input_expression()
            result = eval_expression.eval_expression(a, b, action)
        except Exception as error:
            error_logger.logger.exception("Ошибка при выполнении калькулятора")
            output_handler.output_error(str(error))
            print("Ошибка сохранена в errors.log.\n")
            continue
        else:
            output_handler.output_result(a, b, action, result)
            break

if __name__ == "__main__":
    main()
