# Copyright 2014 Google Inc. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

{
  'includes': [
    './common.gypi',
  ],
  'targets': [
    {
      'target_name': 'libdisasm',
      'type': 'static_library',
      'sources': [
        './deps/breakpad/src/third_party/libdisasm/ia32_implicit.c',
        './deps/breakpad/src/third_party/libdisasm/ia32_implicit.h',
        './deps/breakpad/src/third_party/libdisasm/ia32_insn.c',
        './deps/breakpad/src/third_party/libdisasm/ia32_insn.h',
        './deps/breakpad/src/third_party/libdisasm/ia32_invariant.c',
        './deps/breakpad/src/third_party/libdisasm/ia32_invariant.h',
        './deps/breakpad/src/third_party/libdisasm/ia32_modrm.c',
        './deps/breakpad/src/third_party/libdisasm/ia32_modrm.h',
        './deps/breakpad/src/third_party/libdisasm/ia32_opcode_tables.c',
        './deps/breakpad/src/third_party/libdisasm/ia32_opcode_tables.h',
        './deps/breakpad/src/third_party/libdisasm/ia32_operand.c',
        './deps/breakpad/src/third_party/libdisasm/ia32_operand.h',
        './deps/breakpad/src/third_party/libdisasm/ia32_reg.c',
        './deps/breakpad/src/third_party/libdisasm/ia32_reg.h',
        './deps/breakpad/src/third_party/libdisasm/ia32_settings.c',
        './deps/breakpad/src/third_party/libdisasm/ia32_settings.h',
        './deps/breakpad/src/third_party/libdisasm/libdis.h',
        './deps/breakpad/src/third_party/libdisasm/qword.h',
        './deps/breakpad/src/third_party/libdisasm/x86_disasm.c',
        './deps/breakpad/src/third_party/libdisasm/x86_format.c',
        './deps/breakpad/src/third_party/libdisasm/x86_imm.c',
        './deps/breakpad/src/third_party/libdisasm/x86_imm.h',
        './deps/breakpad/src/third_party/libdisasm/x86_insn.c',
        './deps/breakpad/src/third_party/libdisasm/x86_misc.c',
        './deps/breakpad/src/third_party/libdisasm/x86_operand_list.c',
        './deps/breakpad/src/third_party/libdisasm/x86_operand_list.h',
      ],
    },
  ],
}
