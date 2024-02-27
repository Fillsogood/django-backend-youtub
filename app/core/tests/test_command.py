from django.test import SimpleTestCase
from django.db.utils import OperationalError
from unittest.mock import patch
from django.core.management import call_command
from psycopg2 import OperationalError as Psycopg2OpError


# 데이터베이스 연결 시뮬레이션
@patch('django.db.utils.ConnectionHandler.__getitem__')
class CommandTests(SimpleTestCase):
    # db 연결에 한 번에 성공했을 때
    def test_wait_for_db_ready(self, patched_getitem):
        # ConnectionHandler.__getitem__이 한 번 호출되었는지 확인
        patched_getitem.return_value = True
        call_command('wait_for_db')
        self.assertEqual(patched_getitem.call_count, 1)

    # db 연결에 지연됐을 때
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_getitem):
        patched_getitem.side_effect = [Psycopg2OpError] \
            + [OperationalError] * 5 + [True]
        call_command('wait_for_db')
        self.assertEqual(patched_getitem.call_count, 7)
