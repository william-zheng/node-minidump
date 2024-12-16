{
  'target_defaults': {
    'target_conditions': [
      ['OS=="mac"', {
        'defines': ['HAVE_MACH_O_NLIST_H'],
      }],
      ['OS=="linux"', {
        # Assume glibc.
        'defines': ['HAVE_A_OUT_H', 'HAVE_GETCONTEXT'],
        'sources!': [
          # 'linux/breakpad_getcontext.S',
          # 'linux/breakpad_getcontext.h',
          'linux/breakpad_getcontext_unittest.cc',
        ],
      }],
      ['OS!="android"', {'sources/': [['exclude', '(^|/)android/']]}],
      ['OS!="linux"', {'sources/': [['exclude', '(^|/)linux/']]}],
      ['OS!="mac"', {'sources/': [['exclude', '(^|/)mac/']]}],
      ['OS!="solaris"', {'sources/': [['exclude', '(^|/)solaris/']]}],
      ['OS!="win"', {'sources/': [['exclude', '(^|/)windows/']]}],
    ],
  },
  'targets': [
    {
      'target_name': 'common',
      'type': 'static_library',
      "sources": [
        './deps/breakpad/src/common/basictypes.h', # ??
        './deps/breakpad/src/common/byte_cursor.h', # ??
        './deps/breakpad/src/common/dwarf/bytereader-inl.h', # src_common_dumper_unittest_SOURCES
        
        './deps/breakpad/src/common/dwarf/cfi_assembler.cc', # src_common_mac_macho_reader_unittest_SOURCES src_common_dumper_unittest_SOURCES
        './deps/breakpad/src/common/dwarf/cfi_assembler.h',
        './deps/breakpad/src/common/dwarf/dwarf2enums.h',
        './deps/breakpad/src/common/dwarf/dwarf2reader_test_common.h', # src_common_dumper_unittest_SOURCES
        # './deps/breakpad/src/common/dwarf/functioninfo.cc',
        # './deps/breakpad/src/common/dwarf/functioninfo.h',
        './deps/breakpad/src/common/dwarf/line_state_machine.h',
        './deps/breakpad/src/common/dwarf/types.h',

        './deps/breakpad/src/common/memory_allocator.h',
        './deps/breakpad/src/common/memory_range.h',
        './deps/breakpad/src/common/scoped_ptr.h',

        './deps/breakpad/src/common/symbol_data.h',
        # './deps/breakpad/src/common/test_assembler.cc', # test only
        './deps/breakpad/src/common/test_assembler.h',
        './deps/breakpad/src/common/unordered.h',
        './deps/breakpad/src/common/using_std_string.h',
      ],
      "conditions": [
        [ "OS=='mac' or OS=='linux'", {
          "sources": [
            './deps/breakpad/src/common/dwarf/bytereader.cc', # src_tools_linux_dump_syms_dump_syms_SOURCES src_tools_mac_dump_syms_dump_syms_mac_SOURCES
            './deps/breakpad/src/common/dwarf/bytereader.h',
            './deps/breakpad/src/common/dwarf/dwarf2diehandler.cc', # src_tools_mac_dump_syms_dump_syms_mac_SOURCES src_tools_linux_dump_syms_dump_syms_SOURCES
            './deps/breakpad/src/common/dwarf/dwarf2diehandler.h',
            './deps/breakpad/src/common/dwarf/dwarf2reader.cc', # src_tools_linux_dump_syms_dump_syms_SOURCES src_tools_mac_dump_syms_dump_syms_mac_SOURCES
            './deps/breakpad/src/common/dwarf/dwarf2reader.h',
            './deps/breakpad/src/common/dwarf/elf_reader.cc', # src_tools_linux_dump_syms_dump_syms_SOURCES # src_tools_mac_dump_syms_dump_syms_mac_SOURCES
            './deps/breakpad/src/common/dwarf/elf_reader.h',
            './deps/breakpad/src/common/dwarf_cfi_to_module.cc', # src_tools_linux_dump_syms_dump_syms_SOURCES src_tools_mac_dump_syms_dump_syms_mac_SOURCES
            './deps/breakpad/src/common/dwarf_cfi_to_module.h',
            './deps/breakpad/src/common/dwarf_cu_to_module.cc', # src_tools_linux_dump_syms_dump_syms_SOURCES src_tools_mac_dump_syms_dump_syms_mac_SOURCES
            './deps/breakpad/src/common/dwarf_cu_to_module.h',
            './deps/breakpad/src/common/dwarf_line_to_module.cc', # src_tools_linux_dump_syms_dump_syms_SOURCES src_tools_mac_dump_syms_dump_syms_mac_SOURCES
            './deps/breakpad/src/common/dwarf_line_to_module.h',
            './deps/breakpad/src/common/language.cc', # src_tools_linux_dump_syms_dump_syms_SOURCES  src_tools_mac_dump_syms_dump_syms_mac_SOURCES
            './deps/breakpad/src/common/language.h',
            './deps/breakpad/src/common/md5.cc', # src_client_linux_libbreakpad_client_a_SOURCES src_tools_mac_dump_syms_dump_syms_mac_SOURCES
            './deps/breakpad/src/common/md5.h',
            './deps/breakpad/src/common/path_helper.cc', # linux mac
            './deps/breakpad/src/common/module.cc', # src_tools_linux_dump_syms_dump_syms_SOURCES  src_tools_mac_dump_syms_dump_syms_mac_SOURCES
            './deps/breakpad/src/common/module.h',
            './deps/breakpad/src/common/stabs_reader.cc', # src_tools_linux_dump_syms_dump_syms_SOURCES  src_tools_mac_dump_syms_dump_syms_mac_SOURCES
            './deps/breakpad/src/common/stabs_reader.h',
            './deps/breakpad/src/common/stabs_to_module.cc', # src_tools_linux_dump_syms_dump_syms_SOURCES src_tools_mac_dump_syms_dump_syms_mac_SOURCES
            './deps/breakpad/src/common/stabs_to_module.h',

          ],
        }],
        [ "OS=='mac'", {
          "sources": [
            './deps/breakpad/src/common/simple_string_dictionary.cc', # mac ?
            './deps/breakpad/src/common/simple_string_dictionary.h',
            # './deps/breakpad/src/common/long_string_dictionary.cc', # mac ?
            # './deps/breakpad/src/common/long_string_dictionary.h',
            './deps/breakpad/src/common/mac/arch_utilities.cc', # src_tools_mac_dump_syms_dump_syms_mac_SOURCES
            './deps/breakpad/src/common/mac/arch_utilities.h',
            './deps/breakpad/src/common/mac/bootstrap_compat.cc', # mac ?
            './deps/breakpad/src/common/mac/bootstrap_compat.h',
            './deps/breakpad/src/common/mac/byteswap.h',
            './deps/breakpad/src/common/mac/dump_syms.h',
            './deps/breakpad/src/common/mac/dump_syms.cc', # mac ?
            './deps/breakpad/src/common/mac/file_id.cc',
            './deps/breakpad/src/common/mac/file_id.h',
            './deps/breakpad/src/common/mac/GTMDefines.h',
            './deps/breakpad/src/common/mac/GTMLogger.h',
            './deps/breakpad/src/common/mac/GTMLogger.m',
            './deps/breakpad/src/common/mac/HTTPMultipartUpload.h',
            './deps/breakpad/src/common/mac/HTTPMultipartUpload.m',
            './deps/breakpad/src/common/mac/MachIPC.h',
            './deps/breakpad/src/common/mac/MachIPC.mm',
            './deps/breakpad/src/common/mac/macho_id.cc',
            './deps/breakpad/src/common/mac/macho_id.h',
            './deps/breakpad/src/common/mac/macho_reader.cc',
            './deps/breakpad/src/common/mac/macho_reader.h',
            './deps/breakpad/src/common/mac/macho_utilities.cc',
            './deps/breakpad/src/common/mac/macho_utilities.h',
            './deps/breakpad/src/common/mac/macho_walker.cc',
            './deps/breakpad/src/common/mac/macho_walker.h',
            './deps/breakpad/src/common/mac/scoped_task_suspend-inl.h',
            './deps/breakpad/src/common/mac/string_utilities.cc',
            './deps/breakpad/src/common/mac/string_utilities.h',
            './deps/breakpad/src/common/mac/super_fat_arch.h',
          ],
        }],
        [ "OS=='win'", {
          "sources": [
            './src/windows/path_helper.cc',
            # './deps/breakpad/src/common/windows/common_windows.gyp',
            # './deps/breakpad/src/common/windows/dia_util.cc',
            # './deps/breakpad/src/common/windows/dia_util.h',
            './deps/breakpad/src/common/windows/guid_string.cc',
            './deps/breakpad/src/common/windows/guid_string.h',
            './deps/breakpad/src/common/windows/http_upload.cc',
            './deps/breakpad/src/common/windows/http_upload.h',
            # './deps/breakpad/src/common/windows/omap.cc',
            # './deps/breakpad/src/common/windows/omap.h',
            './deps/breakpad/src/common/windows/omap_internal.h',
            './deps/breakpad/src/common/windows/pdb_source_line_writer.cc',
            './deps/breakpad/src/common/windows/pdb_source_line_writer.h',
            './deps/breakpad/src/common/windows/string_utils-inl.h',
            './deps/breakpad/src/common/windows/string_utils.cc',
          ],
          
          'dependencies': [
            'common_windows.gyp:dia_sdk',
          ],
        }],
        [ "OS=='linux'", {
          "sources": [
            './deps/breakpad/src/common/convert_UTF.cc', # mac 报错
            './deps/breakpad/src/common/convert_UTF.h',

            './deps/breakpad/src/common/string_conversion.cc', # src_client_linux_libbreakpad_client_a_SOURCES mac
            './deps/breakpad/src/common/string_conversion.h',

            # './deps/breakpad/src/common/linux/breakpad_getcontext.S',
            # './deps/breakpad/src/common/linux/breakpad_getcontext.h',
            './deps/breakpad/src/common/linux/crc32.cc',
            './deps/breakpad/src/common/linux/crc32.h',
            './deps/breakpad/src/common/linux/dump_symbols.cc',
            './deps/breakpad/src/common/linux/dump_symbols.h',
            './deps/breakpad/src/common/linux/eintr_wrapper.h',
            './deps/breakpad/src/common/linux/elf_core_dump.cc',
            './deps/breakpad/src/common/linux/elf_core_dump.h',
            './deps/breakpad/src/common/linux/elf_gnu_compat.h',
            './deps/breakpad/src/common/linux/elf_symbols_to_module.cc',
            './deps/breakpad/src/common/linux/elf_symbols_to_module.h',
            './deps/breakpad/src/common/linux/elfutils-inl.h',
            './deps/breakpad/src/common/linux/elfutils.cc',
            './deps/breakpad/src/common/linux/elfutils.h',
            './deps/breakpad/src/common/linux/file_id.cc',
            './deps/breakpad/src/common/linux/file_id.h',
            './deps/breakpad/src/common/linux/google_crashdump_uploader.cc',
            './deps/breakpad/src/common/linux/google_crashdump_uploader.h',
            './deps/breakpad/src/common/linux/guid_creator.cc',
            './deps/breakpad/src/common/linux/guid_creator.h',
            './deps/breakpad/src/common/linux/http_upload.cc',
            './deps/breakpad/src/common/linux/http_upload.h',
            './deps/breakpad/src/common/linux/ignore_ret.h',
            './deps/breakpad/src/common/linux/libcurl_wrapper.cc',
            './deps/breakpad/src/common/linux/libcurl_wrapper.h',
            './deps/breakpad/src/common/linux/linux_libc_support.cc',
            './deps/breakpad/src/common/linux/linux_libc_support.h',
            './deps/breakpad/src/common/linux/memory_mapped_file.cc',
            './deps/breakpad/src/common/linux/memory_mapped_file.h',
            './deps/breakpad/src/common/linux/safe_readlink.cc',
            './deps/breakpad/src/common/linux/safe_readlink.h',
            './deps/breakpad/src/common/linux/symbol_collector_client.cc',
            './deps/breakpad/src/common/linux/symbol_collector_client.h',
            './deps/breakpad/src/common/linux/synth_elf.cc',
            './deps/breakpad/src/common/linux/synth_elf.h',
          ],
        }],
        [ "OS=='android'", {
          "sources": [
            './deps/breakpad/src/common/android/include/elf.h',
            './deps/breakpad/src/common/android/include/link.h',
            './deps/breakpad/src/common/android/include/stab.h',
            './deps/breakpad/src/common/android/include/sys/procfs.h',
            './deps/breakpad/src/common/android/include/sys/user.h',
            './deps/breakpad/src/common/android/testing/include/wchar.h',
            './deps/breakpad/src/common/android/testing/mkdtemp.h',
            './deps/breakpad/src/common/android/testing/pthread_fixes.h',
          ],
        }],
        [ "OS=='solaris'", {
          "sources": [
            './deps/breakpad/src/common/solaris/dump_symbols.cc',
            './deps/breakpad/src/common/solaris/dump_symbols.h',
            './deps/breakpad/src/common/solaris/file_id.cc',
            './deps/breakpad/src/common/solaris/file_id.h',
            './deps/breakpad/src/common/solaris/guid_creator.cc',
            './deps/breakpad/src/common/solaris/guid_creator.h',
            './deps/breakpad/src/common/solaris/message_output.h',
          ],
        }],
      ],
      'include_dirs': [
        './deps/breakpad/src/',
      ],
    },
  ],
}