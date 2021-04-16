def make_shirt(size_type='l', text_message='I love Python.'):
    print(f"Make a shirt size {size_type.title()}, with the message: '{text_message.title()}'.")

make_shirt()
make_shirt(size_type='m')
make_shirt('s', 'not at all')