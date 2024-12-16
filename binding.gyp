# {
#     'target_name': 'All',
#     'type': 'none',
#     'dependencies': [
#         # '../common/common.gyp:*',
#         './deps/breakpad/src/processor/processor.gyp::processor',
#         # '../tools/tools.gyp:*',
#     ],
# }

{
  'target_defaults': {
    'include_dirs': [
      './deps/breakpad/src/',
    ],
  },
  'targets': [
    {
      'target_name': 'minidump_dump',
      'type': 'executable',
      'dependencies': [
        'processor',
      ],
      "conditions": [
        [ "OS!='win'", {
          "sources": [
            './deps/breakpad/src/processor/minidump_dump.cc',
          ],
        }],
        [ "OS=='win'", {
          "sources": [
              './src/windows/minidump_dump.cc',
              './src/windows/getopt.c',
          ],
          'include_dirs': [
            './src/windows/',
          ],
        }],
      ],
    },
    {
      'target_name': 'minidump_stackwalk',
      'type': 'executable',
      # 'sources': [
      #   './deps/breakpad/src/processor/minidump_stackwalk.cc',
      # ],
      'dependencies': [
        'processor',
      ],
      "conditions": [
        [ "OS!='win'", {
          "sources": [
            './deps/breakpad/src/processor/minidump_stackwalk.cc',
          ],
        }],
        [ "OS=='win'", {
          "sources": [
              './src/windows/minidump_stackwalk.cc',
              './src/windows/getopt.c',
              # './src/windows/path_helper.cc',
          ],
          'include_dirs': [
            './src/windows/',
          ],
        }],
      ],
    },
    # {
    #   'target_name': 'dump_syms',
    #   'type': 'executable',
    #   'sources': [
    #   ],
    #   "conditions": [
    #     [ "OS!='win'", {
    #       "sources": [
    #         './deps/breakpad/src/processor/minidump_stackwalk.cc',
    #       ],
    #     }],
    #     [ "OS=='win'", {
    #       "sources": [
    #         './deps/breakpad/src/tools/windows/dump_syms/dump_syms.cc',
    #         # './src/windows/getopt.c',
    #       ],
    #       'includes': [
    #         './common.gypi',
    #       ],
    #       'dependencies': [
    #         './common_windows.gyp:common_windows_lib',
    #       ],
    #     }],
    #   ],
    # },
    {
      'target_name': 'processor',
      'type': 'static_library',
      'sources': [
        './deps/breakpad/src/processor/address_map-inl.h', # src_libbreakpad_a_SOURCES
        './deps/breakpad/src/processor/address_map.h', # src_libbreakpad_a_SOURCES
        './deps/breakpad/src/processor/basic_code_module.h',
        './deps/breakpad/src/processor/basic_code_modules.cc',
        './deps/breakpad/src/processor/basic_code_modules.h',
        './deps/breakpad/src/processor/basic_source_line_resolver.cc',
        './deps/breakpad/src/processor/basic_source_line_resolver_types.h',
        './deps/breakpad/src/processor/call_stack.cc',
        './deps/breakpad/src/processor/cfi_frame_info-inl.h',
        './deps/breakpad/src/processor/cfi_frame_info.cc',
        './deps/breakpad/src/processor/cfi_frame_info.h',
        './deps/breakpad/src/processor/contained_range_map-inl.h',
        './deps/breakpad/src/processor/contained_range_map.h',
        './deps/breakpad/src/processor/convert_old_arm64_context.cc',
        './deps/breakpad/src/processor/convert_old_arm64_context.h',
        './deps/breakpad/src/processor/disassembler_x86.cc',
        './deps/breakpad/src/processor/disassembler_x86.h',
        './deps/breakpad/src/processor/dump_context.cc',
        './deps/breakpad/src/processor/dump_object.cc',
        './deps/breakpad/src/processor/exploitability.cc',
        './deps/breakpad/src/processor/exploitability_linux.cc',
        './deps/breakpad/src/processor/exploitability_linux.h',
        './deps/breakpad/src/processor/exploitability_win.cc',
        './deps/breakpad/src/processor/exploitability_win.h',
        './deps/breakpad/src/processor/fast_source_line_resolver.cc',
        './deps/breakpad/src/processor/fast_source_line_resolver_types.h',
        './deps/breakpad/src/processor/linked_ptr.h',
        './deps/breakpad/src/processor/logging.cc',
        './deps/breakpad/src/processor/logging.h',
        './deps/breakpad/src/processor/map_serializers-inl.h',
        './deps/breakpad/src/processor/map_serializers.h',
        './deps/breakpad/src/processor/microdump.cc', # zwy add
        './deps/breakpad/src/processor/microdump_processor.cc',
        './deps/breakpad/src/processor/minidump.cc',
        './deps/breakpad/src/processor/minidump_processor.cc',
        './deps/breakpad/src/processor/module_comparer.cc',
        './deps/breakpad/src/processor/module_comparer.h',
        './deps/breakpad/src/processor/module_factory.h',
        './deps/breakpad/src/processor/module_serializer.cc',
        './deps/breakpad/src/processor/module_serializer.h',
        './deps/breakpad/src/processor/pathname_stripper.cc',
        './deps/breakpad/src/processor/pathname_stripper.h',
        './deps/breakpad/src/processor/postfix_evaluator-inl.h',
        './deps/breakpad/src/processor/postfix_evaluator.h',
        './deps/breakpad/src/processor/proc_maps_linux.cc',
        './deps/breakpad/src/processor/process_state.cc',
        './deps/breakpad/src/processor/range_map-inl.h',
        './deps/breakpad/src/processor/range_map.h',
        './deps/breakpad/src/processor/simple_serializer-inl.h',
        './deps/breakpad/src/processor/simple_serializer.h',
        './deps/breakpad/src/processor/simple_symbol_supplier.cc',
        './deps/breakpad/src/processor/simple_symbol_supplier.h',
        './deps/breakpad/src/processor/source_line_resolver_base.cc',
        './deps/breakpad/src/processor/source_line_resolver_base_types.h',
        './deps/breakpad/src/processor/stack_frame_cpu.cc',
        './deps/breakpad/src/processor/stack_frame_symbolizer.cc',
        './deps/breakpad/src/processor/stackwalk_common.cc',
        './deps/breakpad/src/processor/stackwalk_common.h',
        './deps/breakpad/src/processor/stackwalker.cc',
        './deps/breakpad/src/processor/stackwalker_address_list.cc',
        './deps/breakpad/src/processor/stackwalker_address_list.h',
        './deps/breakpad/src/processor/stackwalker_amd64.cc',
        './deps/breakpad/src/processor/stackwalker_amd64.h',
        './deps/breakpad/src/processor/stackwalker_arm.cc',
        './deps/breakpad/src/processor/stackwalker_arm.h',
        './deps/breakpad/src/processor/stackwalker_arm64.cc',
        './deps/breakpad/src/processor/stackwalker_arm64.h',
        './deps/breakpad/src/processor/stackwalker_mips.cc',
        './deps/breakpad/src/processor/stackwalker_mips.h',
        './deps/breakpad/src/processor/stackwalker_ppc.cc',
        './deps/breakpad/src/processor/stackwalker_ppc.h',
        './deps/breakpad/src/processor/stackwalker_ppc64.cc',
        './deps/breakpad/src/processor/stackwalker_ppc64.h',
        # './deps/breakpad/src/processor/stackwalker_selftest.cc', # zwy remove
        './deps/breakpad/src/processor/stackwalker_sparc.cc',
        './deps/breakpad/src/processor/stackwalker_sparc.h',
        './deps/breakpad/src/processor/stackwalker_x86.cc',
        './deps/breakpad/src/processor/stackwalker_x86.h',
        './deps/breakpad/src/processor/static_address_map-inl.h',
        './deps/breakpad/src/processor/static_address_map.h',
        './deps/breakpad/src/processor/static_contained_range_map-inl.h',
        './deps/breakpad/src/processor/static_contained_range_map.h',
        './deps/breakpad/src/processor/static_map-inl.h',
        './deps/breakpad/src/processor/static_map.h',
        './deps/breakpad/src/processor/static_map_iterator-inl.h',
        './deps/breakpad/src/processor/static_map_iterator.h',
        './deps/breakpad/src/processor/static_range_map-inl.h',
        './deps/breakpad/src/processor/static_range_map.h',
        './deps/breakpad/src/processor/symbolic_constants_win.cc',
        './deps/breakpad/src/processor/symbolic_constants_win.h',
        # './deps/breakpad/src/processor/synth_minidump.cc', # zwy remove unittest
        # './deps/breakpad/src/processor/synth_minidump.h', # zwy remove unittest
        './deps/breakpad/src/processor/tokenize.cc',
        './deps/breakpad/src/processor/tokenize.h',
        './deps/breakpad/src/processor/windows_frame_info.h',
      ],
      'include_dirs': [
        './deps/breakpad/src/',
      ],
      'dependencies': [
        'common.gyp:common',
        'libdisasm.gyp:libdisasm',
      ],
    },
    {
      'target_name': 'action_after_build',
      'type': 'none',
      'dependencies': [ 
        'minidump_dump',
        'minidump_stackwalk',
      ],
      'conditions': [
            ['OS == "win"', {
                'copies': [
                    {
                    'files': [ '<(PRODUCT_DIR)/minidump_dump.exe' ],
                    'destination': '<(module_root_dir)/bin/win32-<(host_arch)',
                    },
                    {
                    'files': [ '<(PRODUCT_DIR)/minidump_stackwalk.exe' ],
                    'destination': '<(module_root_dir)/bin/win32-<(host_arch)',
                    },
                    {
                    'files': [ '<(module_root_dir)/deps/breakpad/src/tools/windows/binaries/dump_syms.exe' ],
                    'destination': '<(module_root_dir)/bin/win32-<(host_arch)',
                    },
                ],
            }],
            ['OS != "win"', {
                'copies': [
                    {
                    'files': [ '<(PRODUCT_DIR)/minidump_dump' ],
                    'destination': '<(module_root_dir)/bin',
                    },
                    {
                    'files': [ '<(PRODUCT_DIR)/minidump_stackwalk' ],
                    'destination': '<(module_root_dir)/bin',
                    }
                ],
            }],
      ],
    },
  ],
}