require "html-proofer"

def run_linting(dst)
  HTMLProofer.check_directory(
    dst, opts = {
      :check_html => false,
      :check_img_http => true,
      :disable_external => true,
      :report_invalid_tags => true,
    }).run
end

Jekyll::Hooks.register :site, :post_write do |site|
  if site.config["lint"]
    run_linting(site.config["destination"])
  end
end