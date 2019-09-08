# python_study
Python Study


# Python과 C 구현 모듈 I/F 확인
1. Python에서 C로 구현된 함수 단순 호출 ⇐ Python과 C 연동 테스트, Stream Module과의 I/F확인
   1. Python에서 C 함수호출시 인자사용가능여부 및 메모리 영역을 포인트 인자로 넘겨 처리하는데 문제없는지 검토
1. Python에서 C로 구현된 Multi-processor 또는 Multi-Thread 사용 가능성 검토
   1. Python에서 구현된 a를 Multi-Processor 및 Multi-Thread화 시켜 동작 가능한지 확인 ⇐ Python과 Stream Module이 별개로 동작 및 관리 가능한지 확인
   1. Python에서 구현된 b를 기반으로 각 thread 혹은 processor가 사용할 context를 생성하고 다중 context를 처리하는데 문제가 없는지 확인
   1. 각 stream이 사용할 context의 생성/데이터보호/파괴가 가능한지 검토
  생성된 processor나 thread가 특정 물리 processor에 한정되서 동작가능한지 검토 ⇐ python에서 호출
1. 함수포인터 호출 및 queueing 검토
   1. C로 함수 포인터를 queue에 등록하고 queue에 등록된 함수를 호출하는 기능 구현 ⇐ 호출하는 것은 Python
   1. python으로 구현된 함수를 3.i 에 등록하고 호출되는지 확인
   1. 별개의 c로 구현된 모듈(?) 또는 so의 함수를 3.i 에 등록하고 호출되는지 확인
   1. TensorFlow 함수를 c.i에 등록하고 호출되는지 확인
1. 함수포인터 queue 동기화 검토
   1. queue에 등록된 함수들이 동기화를 통해 자동-순차적으로 호출되는지 확인
1. Python & ROS2
   1. Python에서 ROS2용 Publisher와 Subscriber 구현가능한지 검토
   1. 5.i 구현에서 context를 생성하고 c에 인자로 넘겨주는 것이 가능한지 검토

