import logging
import sys
import argparse
from app.runtime.pipeline_runner import PipelineRunner
from app.core.paths import ProjectPaths

# 统一日志格式
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("personaOps-CLI")

def main():
    root_dir = str(ProjectPaths.ROOT)
    
    parser = argparse.ArgumentParser(
        description="personaOps Integrated CLI - The Unified AI Persona Engine",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="Examples:\n"
               "  python3 main.py --mode full\n"
               "  python3 main.py --platform instagram --account my_insta_01\n"
               "  python3 main.py --mode media --persona my_p.json --brand my_b.json\n"
    )
    
    # 默认路径解析为绝对路径
    def_persona = ProjectPaths.get_persona_path("lin_xiaotang.json")
    def_brand = ProjectPaths.get_brand_path("chuan_xing.json")
    def_channel = ProjectPaths.get_channel_path("xhs_main.json")

    # 1. 配置加载参数
    parser.add_argument("--persona", default=def_persona, help="Persona configuration (.json)")
    parser.add_argument("--brand", default=def_brand, help="Brand configuration (.json)")
    parser.add_argument("--channel", default=def_channel, help="Channel configuration (.json)")

    # 2. 运行模式参数
    parser.add_argument("--mode", choices=["full", "plan", "media", "publish"], default="full", 
                        help="Execution mode:\n"
                             "  full:    Planning -> Rendering -> Publishing (Default)\n"
                             "  plan:    Only generate Content Plans\n"
                             "  media:   Render assets based on plan\n"
                             "  publish: Assuming assets ready, only publish")

    # 3. 运行环境覆盖 (Overrides)
    parser.add_argument("--platform", help="Override publishing platform (e.g. xhs, instagram)")
    parser.add_argument("--account", help="Override account ID")
    parser.add_argument("--plan-id", help="Plan ID to use for 'media' mode")
    parser.add_argument("--package-path", help="Local directory path of a MediaPackage for 'publish' mode")
    parser.add_argument("--real", action="store_true", help="Run with REAL drivers (DANGEROUS: actual social publishing)")

    args = parser.parse_args()
    
    # 4. 初始化 Pipeline 引擎并运行
    runner = PipelineRunner(mock_mode=not args.real)
    
    try:
        record = runner.run(
            persona_path=args.persona,
            brand_path=args.brand,
            channel_path=args.channel,
            mode=args.mode,
            platform=args.platform,
            account=args.account,
            plan_id=args.plan_id,
            package_path=args.package_path
        )
        
        if record.status == "success":
            logger.info(f"✅ Pipeline Completed! RunID: {record.id}")
        else:
            logger.error(f"❌ Pipeline Failed! RunID: {record.id} Error: {record.error}")
            sys.exit(1)

    except Exception as e:
        logger.error(f"FATAL CLI ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
