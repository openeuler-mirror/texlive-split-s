%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-s
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source1417:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pslatex.tar.xz
Source1419:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/psnfss.tar.xz
Source1420:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/psnfss.doc.tar.xz
Source1422:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pspicture.tar.xz
Source1423:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pspicture.doc.tar.xz
Source2023:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/prodint.tar.xz
Source2024:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/prodint.doc.tar.xz
Source2025:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/punk.tar.xz
Source2026:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/punk.doc.tar.xz
Source2027:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/punk-latex.tar.xz
Source2028:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/punk-latex.doc.tar.xz
Source2029:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/punknova.tar.xz
Source2030:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/punknova.doc.tar.xz
Source2031:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxtxalfa.tar.xz
Source2032:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxtxalfa.doc.tar.xz
Source2140:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxfonts.tar.xz
Source2141:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxfonts.doc.tar.xz
Source2198:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/psizzl.tar.xz
Source2199:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/psizzl.doc.tar.xz
Source2239:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/psgo.tar.xz
Source2240:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/psgo.doc.tar.xz
Source2580:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-eucl-translation-bg.doc.tar.xz
Source2649:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/presentations-en.doc.tar.xz
Source2774:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/presentations.doc.tar.xz
Source2870:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/psfrag-italian.doc.tar.xz
Source2900:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxbase.tar.xz
Source2901:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxbase.doc.tar.xz
Source2902:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxchfon.tar.xz
Source2903:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxchfon.doc.tar.xz
Source2904:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxcjkcat.tar.xz
Source2905:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxcjkcat.doc.tar.xz
Source2906:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxjahyper.tar.xz
Source2907:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxjahyper.doc.tar.xz
Source2908:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxrubrica.tar.xz
Source2909:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxrubrica.doc.tar.xz
Source2965:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/przechlewski-book.tar.xz
Source2966:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/przechlewski-book.doc.tar.xz
Source3076:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/psfrag.tar.xz
Source3077:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/psfrag.doc.tar.xz
Source3253:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/prerex.tar.xz
Source3254:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/prerex.doc.tar.xz
Source3255:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/productbox.tar.xz
Source3256:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/productbox.doc.tar.xz
Source3258:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxpgfmark.tar.xz
Source3259:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxpgfmark.doc.tar.xz
Source4979:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/preprint.tar.xz
Source4980:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/preprint.doc.tar.xz
Source4982:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pressrelease.tar.xz
Source4983:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pressrelease.doc.tar.xz
Source4985:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/prettyref.tar.xz
Source4986:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/prettyref.doc.tar.xz
Source4988:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/printlen.tar.xz
Source4989:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/printlen.doc.tar.xz
Source4990:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/probsoln.tar.xz
Source4991:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/probsoln.doc.tar.xz
Source4993:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/program.tar.xz
Source4994:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/program.doc.tar.xz
Source4995:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/progress.tar.xz
Source4996:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/progress.doc.tar.xz
Source4997:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/progressbar.tar.xz
Source4998:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/progressbar.doc.tar.xz
Source4999:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/proofread.tar.xz
Source5000:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/proofread.doc.tar.xz
Source5002:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/properties.tar.xz
Source5003:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/properties.doc.tar.xz
Source5004:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/prosper.tar.xz
Source5005:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/prosper.doc.tar.xz
Source5006:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/protex.tar.xz
Source5007:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/protex.doc.tar.xz
Source5008:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/protocol.tar.xz
Source5009:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/protocol.doc.tar.xz
Source5011:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/psfragx.tar.xz
Source5012:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/psfragx.doc.tar.xz
Source5017:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pstool.tar.xz
Source5018:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pstool.doc.tar.xz
Source5020:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxgreeks.tar.xz
Source5021:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxgreeks.doc.tar.xz
Source5023:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/python.tar.xz
Source5024:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/python.doc.tar.xz
Source5886:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/prftree.tar.xz
Source5887:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/prftree.doc.tar.xz
Source5888:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/proba.tar.xz
Source5889:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/proba.doc.tar.xz
Source6108:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/present.tar.xz
Source6109:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/present.doc.tar.xz
Source6130:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/psbao.tar.xz
Source6131:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/psbao.doc.tar.xz
Source6132:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-2dplot.tar.xz
Source6133:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-2dplot.doc.tar.xz
Source6134:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-3d.tar.xz
Source6135:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-3d.doc.tar.xz
Source6137:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-3dplot.tar.xz
Source6138:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-3dplot.doc.tar.xz
Source6139:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-abspos.tar.xz
Source6140:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-abspos.doc.tar.xz
Source6142:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-am.tar.xz
Source6143:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-am.doc.tar.xz
Source6145:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-asr.tar.xz
Source6146:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-asr.doc.tar.xz
Source6147:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-bar.tar.xz
Source6148:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-bar.doc.tar.xz
Source6150:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-barcode.tar.xz
Source6151:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-barcode.doc.tar.xz
Source6152:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-bezier.tar.xz
Source6153:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-bezier.doc.tar.xz
Source6155:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-blur.tar.xz
Source6156:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-blur.doc.tar.xz
Source6158:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-bspline.tar.xz
Source6159:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-bspline.doc.tar.xz
Source6160:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-calendar.tar.xz
Source6161:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-calendar.doc.tar.xz
Source6162:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-circ.tar.xz
Source6163:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-circ.doc.tar.xz
Source6164:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-coil.tar.xz
Source6165:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-coil.doc.tar.xz
Source6166:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-cox.tar.xz
Source6167:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-cox.doc.tar.xz
Source6168:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-dbicons.tar.xz
Source6169:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-dbicons.doc.tar.xz
Source6171:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-diffraction.tar.xz
Source6172:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-diffraction.doc.tar.xz
Source6174:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-electricfield.tar.xz
Source6175:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-electricfield.doc.tar.xz
Source6177:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-eps.tar.xz
Source6178:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-eps.doc.tar.xz
Source6180:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-eucl.tar.xz
Source6181:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-eucl.doc.tar.xz
Source6182:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-exa.tar.xz
Source6183:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-exa.doc.tar.xz
Source6184:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-fill.tar.xz
Source6185:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-fill.doc.tar.xz
Source6187:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-fit.tar.xz
Source6188:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-fit.doc.tar.xz
Source6190:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-fr3d.tar.xz
Source6191:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-fr3d.doc.tar.xz
Source6193:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-fractal.tar.xz
Source6194:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-fractal.doc.tar.xz
Source6195:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-fun.tar.xz
Source6196:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-fun.doc.tar.xz
Source6198:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-func.tar.xz
Source6199:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-func.doc.tar.xz
Source6200:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-gantt.tar.xz
Source6201:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-gantt.doc.tar.xz
Source6202:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-geo.tar.xz
Source6203:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-geo.doc.tar.xz
Source6204:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-ghsb.tar.xz
Source6205:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-ghsb.doc.tar.xz
Source6206:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-gr3d.tar.xz
Source6207:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-gr3d.doc.tar.xz
Source6209:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-grad.tar.xz
Source6210:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-grad.doc.tar.xz
Source6211:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-graphicx.tar.xz
Source6212:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-graphicx.doc.tar.xz
Source6213:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-infixplot.tar.xz
Source6214:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-infixplot.doc.tar.xz
Source6215:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-intersect.tar.xz
Source6216:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-intersect.doc.tar.xz
Source6218:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-jtree.tar.xz
Source6219:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-jtree.doc.tar.xz
Source6220:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-knot.tar.xz
Source6221:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-knot.doc.tar.xz
Source6222:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-labo.tar.xz
Source6223:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-labo.doc.tar.xz
Source6224:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-layout.tar.xz
Source6225:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-layout.doc.tar.xz
Source6226:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-lens.tar.xz
Source6227:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-lens.doc.tar.xz
Source6229:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-light3d.tar.xz
Source6230:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-light3d.doc.tar.xz
Source6232:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-magneticfield.tar.xz
Source6233:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-magneticfield.doc.tar.xz
Source6235:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-math.tar.xz
Source6236:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-math.doc.tar.xz
Source6237:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-mirror.tar.xz
Source6238:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-mirror.doc.tar.xz
Source6239:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-node.tar.xz
Source6240:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-node.doc.tar.xz
Source6241:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-ob3d.tar.xz
Source6242:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-ob3d.doc.tar.xz
Source6244:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-ode.tar.xz
Source6245:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-ode.doc.tar.xz
Source6246:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-optexp.tar.xz
Source6247:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-optexp.doc.tar.xz
Source6249:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-optic.tar.xz
Source6250:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-optic.doc.tar.xz
Source6252:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-osci.tar.xz
Source6253:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-osci.doc.tar.xz
Source6254:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-ovl.tar.xz
Source6255:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-ovl.doc.tar.xz
Source6256:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-pad.tar.xz
Source6257:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-pad.doc.tar.xz
Source6259:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-pdgr.tar.xz
Source6260:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-pdgr.doc.tar.xz
Source6262:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-perspective.tar.xz
Source6263:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-perspective.doc.tar.xz
Source6264:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-platon.tar.xz
Source6265:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-platon.doc.tar.xz
Source6267:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-plot.tar.xz
Source6268:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-plot.doc.tar.xz
Source6269:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-poly.tar.xz
Source6270:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-poly.doc.tar.xz
Source6271:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-pulley.tar.xz
Source6272:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-pulley.doc.tar.xz
Source6274:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-qtree.tar.xz
Source6275:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-qtree.doc.tar.xz
Source6276:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-rubans.tar.xz
Source6277:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-rubans.doc.tar.xz
Source6279:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-sigsys.tar.xz
Source6280:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-sigsys.doc.tar.xz
Source6281:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-slpe.tar.xz
Source6282:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-slpe.doc.tar.xz
Source6284:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-solarsystem.tar.xz
Source6285:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-solarsystem.doc.tar.xz
Source6287:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-solides3d.tar.xz
Source6288:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-solides3d.doc.tar.xz
Source6289:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-soroban.tar.xz
Source6290:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-soroban.doc.tar.xz
Source6292:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-spectra.tar.xz
Source6293:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-spectra.doc.tar.xz
Source6294:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-spirograph.tar.xz
Source6295:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-spirograph.doc.tar.xz
Source6296:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-stru.tar.xz
Source6297:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-stru.doc.tar.xz
Source6298:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-support.doc.tar.xz
Source6299:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-text.tar.xz
Source6300:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-text.doc.tar.xz
Source6302:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-thick.tar.xz
Source6303:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-thick.doc.tar.xz
Source6305:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-tools.tar.xz
Source6306:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-tools.doc.tar.xz
Source6307:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-tree.tar.xz
Source6308:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-tree.doc.tar.xz
Source6310:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-tvz.tar.xz
Source6311:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-tvz.doc.tar.xz
Source6313:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-uml.tar.xz
Source6314:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-uml.doc.tar.xz
Source6316:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-vectorian.tar.xz
Source6317:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-vectorian.doc.tar.xz
Source6318:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-vowel.tar.xz
Source6319:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-vowel.doc.tar.xz
Source6320:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-vue3d.tar.xz
Source6321:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-vue3d.doc.tar.xz
Source6325:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pstricks.tar.xz
Source6326:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pstricks.doc.tar.xz
Source6327:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pstricks-add.tar.xz
Source6328:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pstricks-add.doc.tar.xz
Source6329:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pstricks_calcnotes.doc.tar.xz
Source6481:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pracjourn.tar.xz
Source6482:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pracjourn.doc.tar.xz
Source6484:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/procIAGssymp.tar.xz
Source6485:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/procIAGssymp.doc.tar.xz
Source6486:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/proposal.tar.xz
Source6487:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/proposal.doc.tar.xz
Source6489:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ptptex.tar.xz
Source6490:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ptptex.doc.tar.xz
Source6491:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/psu-thesis.tar.xz
Source6492:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/psu-thesis.doc.tar.xz
Source6709:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pseudocode.tar.xz
Source6710:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pseudocode.doc.tar.xz
Source6768:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ptext.tar.xz
Source6769:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ptext.doc.tar.xz
Source7489:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/prooftrees.tar.xz
Source7490:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/prooftrees.doc.tar.xz
Source7491:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-cie.tar.xz
Source7492:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-cie.doc.tar.xz
Source7582:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ptex-base.tar.xz
Source7583:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ptex-base.doc.tar.xz
Source7584:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ptex-fonts.tar.xz
Source7585:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ptex-fonts.doc.tar.xz
Source7915:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-arrow.tar.xz
Source7916:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-arrow.doc.tar.xz
Source7917:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-geometrictools.tar.xz
Source7918:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-geometrictools.doc.tar.xz
Source7919:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-poker.tar.xz
Source7920:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-poker.doc.tar.xz
Source7921:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-rputover.tar.xz
Source7922:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-rputover.doc.tar.xz
Source7923:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-shell.tar.xz
Source7924:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-shell.doc.tar.xz
Source7925:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-vehicle.tar.xz
Source7926:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-vehicle.doc.tar.xz
Source7927:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pstring.tar.xz
Source7928:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pstring.doc.tar.xz
Source7931:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxtatescale.tar.xz
Source7932:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxtatescale.doc.tar.xz
Source7933:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxufont.tar.xz
Source7934:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pxufont.doc.tar.xz
Source8282:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-antiprism.tar.xz
Source8283:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-antiprism.doc.tar.xz
Source8284:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-calculate.tar.xz
Source8285:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-calculate.doc.tar.xz
Source8286:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-contourplot.tar.xz
Source8287:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-contourplot.doc.tar.xz
Source8288:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-dart.tar.xz
Source8289:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-dart.doc.tar.xz
Source8292:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-spinner.tar.xz
Source8293:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-spinner.doc.tar.xz
Source8296:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pythonhighlight.tar.xz
Source8297:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pythonhighlight.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-pslatex
Provides:       tex-pslatex = %{tl_version}
License:        LPPL
Summary:        Use PostScript fonts by default
Version:        svn16416.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pcrr8rn.map) = %{tl_version}, tex(pcrr7tn.tfm) = %{tl_version}
Provides:       tex(pcrr8rn.tfm) = %{tl_version}, tex(pcrr8tn.tfm) = %{tl_version}
Provides:       tex(pcrr7tn.vf) = %{tl_version}, tex(pcrr8tn.vf) = %{tl_version}
Provides:       tex(pslatex.sty) = %{tl_version}

%description -n texlive-pslatex
A small package that makes LaTeX default to 'standard'
PostScript fonts. It is basically a merger of the times and the
(obsolete) mathptm packages from the psnfss suite. You must
have installed standard LaTeX and the psnfss PostScript fonts
to use this package. The main novel feature is that the pslatex
package tries to compensate for the visual differences between
the Adobe fonts by scaling Helvetica by 90%, and 'condensing'
Courier (i.e. scaling horizontally) by 85%. The package is
supplied with a (unix) shell file for a 'pslatex' command that
allows standard LaTeX documents to be processed, without
needing to edit the file. Note that current psnfss uses a
different technique for scaling Helvetica, and treats Courier
as a lost cause (there are better free fixed-width available
now, than there were when pslatex was designed). As a result,
pslatex is widely considered obsolete.

%package -n texlive-psnfss
Provides:       tex-psnfss = %{tl_version}
License:        LPPL
Summary:        Font support for common PostScript fonts
Version:        svn33946.9.2a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex-graphics, tex(keyval.sty)
Provides:       tex(charter.map) = %{tl_version}, tex(fpls.map) = %{tl_version}
Provides:       tex(pazo.map) = %{tl_version}, tex(psnfss.map) = %{tl_version}
Provides:       tex(utopia.map) = %{tl_version}, tex(8rbch.fd) = %{tl_version}
Provides:       tex(8rpag.fd) = %{tl_version}, tex(8rpbk.fd) = %{tl_version}
Provides:       tex(8rpcr.fd) = %{tl_version}, tex(8rphv.fd) = %{tl_version}
Provides:       tex(8rpnc.fd) = %{tl_version}, tex(8rppl.fd) = %{tl_version}
Provides:       tex(8rptm.fd) = %{tl_version}, tex(8rput.fd) = %{tl_version}
Provides:       tex(8rpzc.fd) = %{tl_version}, tex(avant.sty) = %{tl_version}
Provides:       tex(bookman.sty) = %{tl_version}, tex(chancery.sty) = %{tl_version}
Provides:       tex(charter.sty) = %{tl_version}, tex(courier.sty) = %{tl_version}
Provides:       tex(helvet.sty) = %{tl_version}, tex(mathpazo.sty) = %{tl_version}
Provides:       tex(mathpple.sty) = %{tl_version}, tex(mathptm.sty) = %{tl_version}
Provides:       tex(mathptmx.sty) = %{tl_version}, tex(newcent.sty) = %{tl_version}
Provides:       tex(omlbch.fd) = %{tl_version}, tex(omlpag.fd) = %{tl_version}
Provides:       tex(omlpbk.fd) = %{tl_version}, tex(omlpcr.fd) = %{tl_version}
Provides:       tex(omlphv.fd) = %{tl_version}, tex(omlpnc.fd) = %{tl_version}
Provides:       tex(omlppl.fd) = %{tl_version}, tex(omlptm.fd) = %{tl_version}
Provides:       tex(omlptmcm.fd) = %{tl_version}, tex(omlput.fd) = %{tl_version}
Provides:       tex(omlpzc.fd) = %{tl_version}, tex(omlzplm.fd) = %{tl_version}
Provides:       tex(omlzpple.fd) = %{tl_version}, tex(omlztmcm.fd) = %{tl_version}
Provides:       tex(omsbch.fd) = %{tl_version}, tex(omspag.fd) = %{tl_version}
Provides:       tex(omspbk.fd) = %{tl_version}, tex(omspcr.fd) = %{tl_version}
Provides:       tex(omsphv.fd) = %{tl_version}, tex(omspnc.fd) = %{tl_version}
Provides:       tex(omsppl.fd) = %{tl_version}, tex(omsptm.fd) = %{tl_version}
Provides:       tex(omsput.fd) = %{tl_version}, tex(omspzc.fd) = %{tl_version}
Provides:       tex(omspzccm.fd) = %{tl_version}, tex(omszplm.fd) = %{tl_version}
Provides:       tex(omszpple.fd) = %{tl_version}, tex(omsztmcm.fd) = %{tl_version}
Provides:       tex(omxpsycm.fd) = %{tl_version}, tex(omxzplm.fd) = %{tl_version}
Provides:       tex(omxzpple.fd) = %{tl_version}, tex(omxztmcm.fd) = %{tl_version}
Provides:       tex(ot1bch.fd) = %{tl_version}, tex(ot1pag.fd) = %{tl_version}
Provides:       tex(ot1pbk.fd) = %{tl_version}, tex(ot1pcr.fd) = %{tl_version}
Provides:       tex(ot1phv.fd) = %{tl_version}, tex(ot1pnc.fd) = %{tl_version}
Provides:       tex(ot1ppl.fd) = %{tl_version}, tex(ot1pplj.fd) = %{tl_version}
Provides:       tex(ot1pplx.fd) = %{tl_version}, tex(ot1ptm.fd) = %{tl_version}
Provides:       tex(ot1ptmcm.fd) = %{tl_version}, tex(ot1put.fd) = %{tl_version}
Provides:       tex(ot1pzc.fd) = %{tl_version}, tex(ot1zplm.fd) = %{tl_version}
Provides:       tex(ot1zpple.fd) = %{tl_version}, tex(ot1ztmcm.fd) = %{tl_version}
Provides:       tex(palatino.sty) = %{tl_version}, tex(pifont.sty) = %{tl_version}
Provides:       tex(t1bch.fd) = %{tl_version}, tex(t1pag.fd) = %{tl_version}
Provides:       tex(t1pbk.fd) = %{tl_version}, tex(t1pcr.fd) = %{tl_version}
Provides:       tex(t1phv.fd) = %{tl_version}, tex(t1pnc.fd) = %{tl_version}
Provides:       tex(t1ppl.fd) = %{tl_version}, tex(t1pplj.fd) = %{tl_version}
Provides:       tex(t1pplx.fd) = %{tl_version}, tex(t1ptm.fd) = %{tl_version}
Provides:       tex(t1put.fd) = %{tl_version}, tex(t1pzc.fd) = %{tl_version}
Provides:       tex(times.sty) = %{tl_version}, tex(ts1bch.fd) = %{tl_version}
Provides:       tex(ts1pag.fd) = %{tl_version}, tex(ts1pbk.fd) = %{tl_version}
Provides:       tex(ts1pcr.fd) = %{tl_version}, tex(ts1phv.fd) = %{tl_version}
Provides:       tex(ts1pnc.fd) = %{tl_version}, tex(ts1ppl.fd) = %{tl_version}
Provides:       tex(ts1pplj.fd) = %{tl_version}, tex(ts1pplx.fd) = %{tl_version}
Provides:       tex(ts1ptm.fd) = %{tl_version}, tex(ts1put.fd) = %{tl_version}
Provides:       tex(ts1pzc.fd) = %{tl_version}, tex(ufplm.fd) = %{tl_version}
Provides:       tex(ufplmbb.fd) = %{tl_version}, tex(upsy.fd) = %{tl_version}
Provides:       tex(upzd.fd) = %{tl_version}, tex(utopia.sty) = %{tl_version}

%description -n texlive-psnfss
Font definition files, macros and font metrics for freely-
available Adobe Type 1 fonts. The font set consists of the
'LaserWriter 35' set (originally 'freely available' because
embedded in PostScript printers), and a variety of other free
fonts, together with some additions. Note that while many of
the fonts are available in PostScript (and other) printers,
most publishers require fonts embedded in documents, which
requires that you have the fonts in your TeX system.
Fortunately, there are free versions of the fonts from URW
(available in the URW base5 bundle). The base set of text fonts
covered by PSNFSS are: AvantGarde, Bookman, Courier, Helvetica,
New Century Schoolbook, Palatino, Symbol, Times Roman and Zapf
Dingbats. In addition, the fonts Bitstream Charter and Adobe
Utopia are covered (those fonts were contributed to the Public
Domain by their commercial foundries). Separate packages are
provided to load each font for use as main text font. The
packages helvet (which allows Helvetica to be loaded with its
size scaled to something more nearly appropriate for its use as
a Sans-Serif font to match Times) and pifont (which provides
the means to select single glyphs from symbol fonts) are
tailored to special requirements of their fonts. Mathematics
are covered by the mathptmx package, which constructs passable
mathematics from a combination of Times Roman, Symbol and some
glyphs from Computer Modern, and by Pazo Math (optionally
extended with the fpl small-caps and old-style figures fonts)
which uses Palatino as base font, with the mathpazo fonts. The
bundle as a whole is part of the LaTeX 'required' set of
packages.

%package -n texlive-psnfss-doc
Summary:        Documentation for psnfss
Version:        svn33946.9.2a

Provides:       tex-psnfss-doc
AutoReqProv:    No
Requires:       tex-graphics-doc

%description -n texlive-psnfss-doc
Documentation for psnfss

%package -n texlive-pspicture
Provides:       tex-pspicture = %{tl_version}
License:        LPPL
Summary:        PostScript picture support
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pspicture.sty) = %{tl_version}

%description -n texlive-pspicture
A replacement for LaTeX's picture macros, that uses PostScript
\special commands. The package is now largely superseded by
pict2e.

%package -n texlive-pspicture-doc
Summary:        Documentation for pspicture
Version:        svn15878.0

Provides:       tex-pspicture-doc
AutoReqProv:    No

%description -n texlive-pspicture-doc
Documentation for pspicture

%package -n texlive-prodint
Provides:       tex-prodint = %{tl_version}
License:        OFL
Summary:        A font that provides the product integral symbol
Version:        svn21893.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(prodint.map) = %{tl_version}, tex(prodint.tfm) = %{tl_version}
Provides:       tex(prodint.pfb) = %{tl_version}, tex(prodint.sty) = %{tl_version}

%description -n texlive-prodint
Product integrals are to products, as integrals are to sums.
They have been around for more than a hundred years, they have
not become part of the standard mathematician's toolbox,
possibly because no-one invented the right mathematical symbol
for them. The authors have remedied that situation by proposing
the symbol and providing this font.

%package -n texlive-prodint-doc
Summary:        Documentation for prodint
Version:        svn21893.0

Provides:       tex-prodint-doc
AutoReqProv:    No

%description -n texlive-prodint-doc
Documentation for prodint

%package -n texlive-punk
Provides:       tex-punk = %{tl_version}
License:        Knuth
Summary:        Donald Knuth's punk font
Version:        svn27388.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(punk10.tfm) = %{tl_version}, tex(punk12.tfm) = %{tl_version}
Provides:       tex(punk20.tfm) = %{tl_version}, tex(punkbx20.tfm) = %{tl_version}
Provides:       tex(punksl20.tfm) = %{tl_version}

%description -n texlive-punk
A response to the assertion in a lecture that "typography tends
to lag behind other stylistic changes by about 10 years". Knuth
felt it was (in 1988) time to design a replacement for his
designs of the 1970s, and came up with this font! The fonts are
distributed as Metafont source. The package offers LaTeX
support by Rohit Grover, from an original by Sebastian Rahtz,
which is slightly odd in claiming that the fonts are T1-
encoded. A (possibly) more rational support package is to be
found in punk-latex

%package -n texlive-punk-doc
Summary:        Documentation for punk
Version:        svn27388.0

Provides:       tex-punk-doc
AutoReqProv:    No

%description -n texlive-punk-doc
Documentation for punk

%package -n texlive-punk-latex
Provides:       tex-punk-latex = %{tl_version}
License:        GPL+
Summary:        LaTeX support for punk fonts
Version:        svn27389.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ot1pnk.fd) = %{tl_version}, tex(punk.sty) = %{tl_version}

%description -n texlive-punk-latex
The package and .fd file provide support for Knuth's punk
fonts. That bundle also offers support within LaTeX; the
present package is to be preferred.

%package -n texlive-punk-latex-doc
Summary:        Documentation for punk-latex
Version:        svn27389.1.1

Provides:       tex-punk-latex-doc
AutoReqProv:    No

%description -n texlive-punk-latex-doc
Documentation for punk-latex

%package -n texlive-punknova
Provides:       tex-punknova = %{tl_version}
License:        Punknova
Summary:        OpenType version of Knuth's Punk font
Version:        svn24649.1.003

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(punknova-bold.otf) = %{tl_version}, tex(punknova-boldslanted.otf) = %{tl_version}
Provides:       tex(punknova-regular.otf) = %{tl_version}
Provides:       tex(punknova-slanted.otf) = %{tl_version}

%description -n texlive-punknova
The font was generated from a MetaPost version of the sources
of the 'original' punk font. Knuth's original fonts generated
different shapes at random. This isn't actually possible in an
OpenType font; rather, the font contains several variants of
each glyph, and uses the OpenType randomize function to select
a variant for each invocation.

%package -n texlive-punknova-doc
Summary:        Documentation for punknova
Version:        svn24649.1.003

Provides:       tex-punknova-doc
AutoReqProv:    No

%description -n texlive-punknova-doc
Documentation for punknova

%package -n texlive-pxtxalfa
Provides:       tex-pxtxalfa = %{tl_version}
License:        LPPL
Summary:        Virtual maths alphabets based on pxfonts and txfonts
Version:        svn23682.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(xkeyval.sty)
Provides:       tex(pxtx.map) = %{tl_version}, tex(pxb-ds.tfm) = %{tl_version}
Provides:       tex(pxr-ds.tfm) = %{tl_version}, tex(rtxmia.tfm) = %{tl_version}
Provides:       tex(txb-cal.tfm) = %{tl_version}, tex(txb-frak.tfm) = %{tl_version}
Provides:       tex(txb-of.tfm) = %{tl_version}, tex(txr-cal.tfm) = %{tl_version}
Provides:       tex(txr-ds.tfm) = %{tl_version}, tex(txr-frak.tfm) = %{tl_version}
Provides:       tex(txr-of.tfm) = %{tl_version}, tex(pxb-ds.vf) = %{tl_version}
Provides:       tex(pxr-ds.vf) = %{tl_version}, tex(txb-cal.vf) = %{tl_version}
Provides:       tex(txb-frak.vf) = %{tl_version}, tex(txb-of.vf) = %{tl_version}
Provides:       tex(txr-cal.vf) = %{tl_version}, tex(txr-ds.vf) = %{tl_version}
Provides:       tex(txr-frak.vf) = %{tl_version}, tex(txr-of.vf) = %{tl_version}
Provides:       tex(px-ds.sty) = %{tl_version}, tex(pxtx-cal.sty) = %{tl_version}
Provides:       tex(pxtx-frak.sty) = %{tl_version}, tex(tx-of.sty) = %{tl_version}
Provides:       tex(upx-ds.fd) = %{tl_version}, tex(utx-cal.fd) = %{tl_version}
Provides:       tex(utx-frak.fd) = %{tl_version}, tex(utx-of.fd) = %{tl_version}

%description -n texlive-pxtxalfa
The package provides virtual math alphabets based on pxfonts
and txfonts, with LaTeX support files and adjusted metrics. The
mathalfa package offers support for this collection.

%package -n texlive-pxtxalfa-doc
Summary:        Documentation for pxtxalfa
Version:        svn23682.1

Provides:       tex-pxtxalfa-doc
AutoReqProv:    No

%description -n texlive-pxtxalfa-doc
Documentation for pxtxalfa

%package -n texlive-pxfonts
Provides:       tex-pxfonts = %{tl_version}
License:        GPL+
Summary:        Palatino-like fonts in support of mathematics
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(pxfonts.map) = %{tl_version}, tex(pxr.map) = %{tl_version}
Provides:       tex(pxr1.map) = %{tl_version}, tex(pxr2.map) = %{tl_version}
Provides:       tex(pxr3.map) = %{tl_version}, tex(p1xb.tfm) = %{tl_version}
Provides:       tex(p1xbi.tfm) = %{tl_version}, tex(p1xbsc.tfm) = %{tl_version}
Provides:       tex(p1xbsl.tfm) = %{tl_version}, tex(p1xi.tfm) = %{tl_version}
Provides:       tex(p1xr.tfm) = %{tl_version}, tex(p1xsc.tfm) = %{tl_version}
Provides:       tex(p1xsl.tfm) = %{tl_version}, tex(pcxb.tfm) = %{tl_version}
Provides:       tex(pcxbi.tfm) = %{tl_version}, tex(pcxbsl.tfm) = %{tl_version}
Provides:       tex(pcxi.tfm) = %{tl_version}, tex(pcxr.tfm) = %{tl_version}
Provides:       tex(pcxsl.tfm) = %{tl_version}, tex(pxb.tfm) = %{tl_version}
Provides:       tex(pxbex.tfm) = %{tl_version}, tex(pxbexa.tfm) = %{tl_version}
Provides:       tex(pxbi.tfm) = %{tl_version}, tex(pxbmi.tfm) = %{tl_version}
Provides:       tex(pxbmi1.tfm) = %{tl_version}, tex(pxbmia.tfm) = %{tl_version}
Provides:       tex(pxbsc.tfm) = %{tl_version}, tex(pxbsl.tfm) = %{tl_version}
Provides:       tex(pxbsy.tfm) = %{tl_version}, tex(pxbsya.tfm) = %{tl_version}
Provides:       tex(pxbsyb.tfm) = %{tl_version}, tex(pxbsyc.tfm) = %{tl_version}
Provides:       tex(pxex.tfm) = %{tl_version}, tex(pxexa.tfm) = %{tl_version}
Provides:       tex(pxi.tfm) = %{tl_version}, tex(pxmi.tfm) = %{tl_version}
Provides:       tex(pxmi1.tfm) = %{tl_version}, tex(pxmia.tfm) = %{tl_version}
Provides:       tex(pxr.tfm) = %{tl_version}, tex(pxsc.tfm) = %{tl_version}
Provides:       tex(pxsl.tfm) = %{tl_version}, tex(pxsy.tfm) = %{tl_version}
Provides:       tex(pxsya.tfm) = %{tl_version}, tex(pxsyb.tfm) = %{tl_version}
Provides:       tex(pxsyc.tfm) = %{tl_version}, tex(rpcxb.tfm) = %{tl_version}
Provides:       tex(rpcxbi.tfm) = %{tl_version}, tex(rpcxbsl.tfm) = %{tl_version}
Provides:       tex(rpcxi.tfm) = %{tl_version}, tex(rpcxr.tfm) = %{tl_version}
Provides:       tex(rpcxsl.tfm) = %{tl_version}, tex(rpxb.tfm) = %{tl_version}
Provides:       tex(rpxbi.tfm) = %{tl_version}, tex(rpxbmi.tfm) = %{tl_version}
Provides:       tex(rpxbsc.tfm) = %{tl_version}, tex(rpxbsl.tfm) = %{tl_version}
Provides:       tex(rpxi.tfm) = %{tl_version}, tex(rpxmi.tfm) = %{tl_version}
Provides:       tex(rpxpplb.tfm) = %{tl_version}, tex(rpxpplbi.tfm) = %{tl_version}
Provides:       tex(rpxpplbo.tfm) = %{tl_version}, tex(rpxpplr.tfm) = %{tl_version}
Provides:       tex(rpxpplri.tfm) = %{tl_version}, tex(rpxpplro.tfm) = %{tl_version}
Provides:       tex(rpxr.tfm) = %{tl_version}, tex(rpxsc.tfm) = %{tl_version}
Provides:       tex(rpxsl.tfm) = %{tl_version}, tex(pxbex.pfb) = %{tl_version}
Provides:       tex(pxbexa.pfb) = %{tl_version}, tex(pxbmia.pfb) = %{tl_version}
Provides:       tex(pxbsy.pfb) = %{tl_version}, tex(pxbsya.pfb) = %{tl_version}
Provides:       tex(pxbsyb.pfb) = %{tl_version}, tex(pxbsyc.pfb) = %{tl_version}
Provides:       tex(pxex.pfb) = %{tl_version}, tex(pxexa.pfb) = %{tl_version}
Provides:       tex(pxmia.pfb) = %{tl_version}, tex(pxsy.pfb) = %{tl_version}
Provides:       tex(pxsya.pfb) = %{tl_version}, tex(pxsyb.pfb) = %{tl_version}
Provides:       tex(pxsyc.pfb) = %{tl_version}, tex(rpcxb.pfb) = %{tl_version}
Provides:       tex(rpcxbi.pfb) = %{tl_version}, tex(rpcxi.pfb) = %{tl_version}
Provides:       tex(rpcxr.pfb) = %{tl_version}, tex(rpxb.pfb) = %{tl_version}
Provides:       tex(rpxbi.pfb) = %{tl_version}, tex(rpxbmi.pfb) = %{tl_version}
Provides:       tex(rpxbsc.pfb) = %{tl_version}, tex(rpxi.pfb) = %{tl_version}
Provides:       tex(rpxmi.pfb) = %{tl_version}, tex(rpxr.pfb) = %{tl_version}
Provides:       tex(rpxsc.pfb) = %{tl_version}, tex(p1xb.vf) = %{tl_version}
Provides:       tex(p1xbi.vf) = %{tl_version}, tex(p1xbsc.vf) = %{tl_version}
Provides:       tex(p1xbsl.vf) = %{tl_version}, tex(p1xi.vf) = %{tl_version}
Provides:       tex(p1xr.vf) = %{tl_version}, tex(p1xsc.vf) = %{tl_version}
Provides:       tex(p1xsl.vf) = %{tl_version}, tex(pcxb.vf) = %{tl_version}
Provides:       tex(pcxbi.vf) = %{tl_version}, tex(pcxbsl.vf) = %{tl_version}
Provides:       tex(pcxi.vf) = %{tl_version}, tex(pcxr.vf) = %{tl_version}
Provides:       tex(pcxsl.vf) = %{tl_version}, tex(pxb.vf) = %{tl_version}
Provides:       tex(pxbi.vf) = %{tl_version}, tex(pxbmi.vf) = %{tl_version}
Provides:       tex(pxbmi1.vf) = %{tl_version}, tex(pxbsc.vf) = %{tl_version}
Provides:       tex(pxbsl.vf) = %{tl_version}, tex(pxi.vf) = %{tl_version}
Provides:       tex(pxmi.vf) = %{tl_version}, tex(pxmi1.vf) = %{tl_version}
Provides:       tex(pxr.vf) = %{tl_version}, tex(pxsc.vf) = %{tl_version}
Provides:       tex(pxsl.vf) = %{tl_version}, tex(omlpxmi.fd) = %{tl_version}
Provides:       tex(omlpxr.fd) = %{tl_version}, tex(omspxr.fd) = %{tl_version}
Provides:       tex(omspxsy.fd) = %{tl_version}, tex(omxpxex.fd) = %{tl_version}
Provides:       tex(ot1pxr.fd) = %{tl_version}, tex(ot1pxss.fd) = %{tl_version}
Provides:       tex(ot1pxtt.fd) = %{tl_version}, tex(pxfonts.sty) = %{tl_version}
Provides:       tex(t1pxr.fd) = %{tl_version}, tex(t1pxss.fd) = %{tl_version}
Provides:       tex(t1pxtt.fd) = %{tl_version}, tex(ts1pxr.fd) = %{tl_version}
Provides:       tex(ts1pxss.fd) = %{tl_version}, tex(ts1pxtt.fd) = %{tl_version}
Provides:       tex(upxexa.fd) = %{tl_version}, tex(upxmia.fd) = %{tl_version}
Provides:       tex(upxr.fd) = %{tl_version}, tex(upxss.fd) = %{tl_version}
Provides:       tex(upxsya.fd) = %{tl_version}, tex(upxsyb.fd) = %{tl_version}
Provides:       tex(upxsyc.fd) = %{tl_version}, tex(upxtt.fd) = %{tl_version}

%description -n texlive-pxfonts
Pxfonts supplies virtual text roman fonts using Adobe Palatino
(or URWPalladioL) with some modified and additional text
symbols in the OT1, T1, and TS1 encodings; maths alphabets
using Palatino/Palladio; maths fonts providing all the symbols
of the Computer Modern and AMS fonts, including all the Greek
capital letters from CMR; and additional maths fonts of various
other symbols. The set is complemented by a sans-serif set of
text fonts, based on Helvetica/NimbusSanL, and a monospace set
derived from the parallel TX font set. All the fonts are in
Type 1 format (AFM and PFB files), and are supported by TeX
metrics (VF and TFM files) and macros for use with LaTeX.

%package -n texlive-pxfonts-doc
Summary:        Documentation for pxfonts
Version:        svn15878.0

Provides:       tex-pxfonts-doc
AutoReqProv:    No

%description -n texlive-pxfonts-doc
Documentation for pxfonts

%package -n texlive-psizzl
Provides:       tex-psizzl = %{tl_version}
License:        LPPL
Summary:        A TeX format for physics papers
Version:        svn15878.0.35

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mypsizzl.tex) = %{tl_version}, tex(psizzl.tex) = %{tl_version}

%description -n texlive-psizzl
PSIZZL is a TeX format for physics papers written at SLAC and
used at several other places. It dates from rather early in the
development of TeX82; as a result, some of the descriptions of
limitations look rather quaint to modern eyes.

%package -n texlive-psizzl-doc
Summary:        Documentation for psizzl
Version:        svn15878.0.35

Provides:       tex-psizzl-doc
AutoReqProv:    No

%description -n texlive-psizzl-doc
Documentation for psizzl

%package -n texlive-psgo
Provides:       tex-psgo = %{tl_version}
License:        LPPL
Summary:        Typeset go diagrams with PSTricks
Version:        svn15878.0.17

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(pst-node.sty), tex(calc.sty), tex(ifthen.sty)
Provides:       tex(psgo.sty) = %{tl_version}

%description -n texlive-psgo
psgo package

%package -n texlive-psgo-doc
Summary:        Documentation for psgo
Version:        svn15878.0.17

Provides:       tex-psgo-doc
AutoReqProv:    No

%description -n texlive-psgo-doc
Documentation for psgo

%package -n texlive-pst-eucl-translation-bg-doc
Summary:        Documentation for pst-eucl-translation-bg
Version:        svn19296.1.3.2

Provides:       tex-pst-eucl-translation-bg-doc
AutoReqProv:    No

%description -n texlive-pst-eucl-translation-bg-doc
Documentation for pst-eucl-translation-bg

%package -n texlive-pxchfon
Provides:       tex-pxchfon = %{tl_version}
License:        MIT
Summary:        Japanese font setup for pLaTeX and upLaTeX
Version:        svn46971
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(atbegshi.sty)
Provides:       tex(cfjar-b-l0j.tfm) = %{tl_version}, tex(cfjar-l-l0j.tfm) = %{tl_version}
Provides:       tex(cfjar-r-l0j.tfm) = %{tl_version}, tex(cfjas-b-l0j.tfm) = %{tl_version}
Provides:       tex(cfjas-r-l0j.tfm) = %{tl_version}, tex(cfjas-x-l0j.tfm) = %{tl_version}
Provides:       tex(r-cfjar-b-l0j.tfm) = %{tl_version}, tex(r-cfjar-l-l0j.tfm) = %{tl_version}
Provides:       tex(r-cfjar-r-l0j.tfm) = %{tl_version}, tex(r-cfjas-b-l0j.tfm) = %{tl_version}
Provides:       tex(r-cfjas-r-l0j.tfm) = %{tl_version}, tex(r-cfjas-x-l0j.tfm) = %{tl_version}
Provides:       tex(cfjar-b-l0j.vf) = %{tl_version}, tex(cfjar-l-l0j.vf) = %{tl_version}
Provides:       tex(cfjar-r-l0j.vf) = %{tl_version}, tex(cfjas-b-l0j.vf) = %{tl_version}
Provides:       tex(cfjas-r-l0j.vf) = %{tl_version}, tex(cfjas-x-l0j.vf) = %{tl_version}
Provides:       tex(pxchfon.sty) = %{tl_version}, tex(pxchfon0.def) = %{tl_version}
Provides:       tex(pxjafont.sty) = %{tl_version}

%description -n texlive-pxchfon
This package enables users to declare in their document which
physical fonts should be used for the standard Japanese
(logical) fonts of pLaTeX and upLaTeX. Font setup is realized
by changing the font mapping of dvipdfmx, and thus users can
use any (monospaced) physical fonts they like, once they
properly install this package, without creating helper files
for each new font. This package also supports setup for the
fonts used in the japanese-otf package.

%package -n texlive-pxchfon-doc
Summary:        Documentation for pxchfon
Version:        svn46971
Provides:       tex-pxchfon-doc
AutoReqProv:    No

%description -n texlive-pxchfon-doc
Documentation for pxchfon

%package -n texlive-pxbase
Provides:       tex-pxbase = %{tl_version}
License:        MIT
Summary:        Tools for use with (u)pLaTeX
Version:        svn44756
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(ifuptex.sty) = %{tl_version}, tex(pxbabel.sty) = %{tl_version}
Provides:       tex(pxbase.def) = %{tl_version}, tex(pxbase.sty) = %{tl_version}
Provides:       tex(pxbasenc.def) = %{tl_version}, tex(pxbsjc.def) = %{tl_version}
Provides:       tex(pxjsfenc.def) = %{tl_version}, tex(upkcat.sty) = %{tl_version}

%description -n texlive-pxbase
The main purpose of this package is to provide auxiliary
functions which are utilized by other packages created by the
same author. It also provides a few user commands to assist in
creating Japanese documents using (u)pLaTeX.

%package -n texlive-pxbase-doc
Summary:        Documentation for pxbase
Version:        svn44756
Provides:       tex-pxbase-doc
AutoReqProv:    No

%description -n texlive-pxbase-doc
Documentation for pxbase

%package -n texlive-pxcjkcat
Provides:       tex-pxcjkcat = %{tl_version}
License:        MIT
Summary:        LaTeX interface for the CJK category codes of upTeX
Version:        svn47266
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(pxcjkcat.sty) = %{tl_version}

%description -n texlive-pxcjkcat
The package provides management of the CJK category code
('kcatcode'> table of the upTeX extended TeX engine. Package
options are available for tailored use in the cases of
documents that are principally written in Japanese, or
principally written in English or other Western languages.

%package -n texlive-pxcjkcat-doc
Summary:        Documentation for pxcjkcat
Version:        svn47266
Provides:       tex-pxcjkcat-doc
AutoReqProv:    No

%description -n texlive-pxcjkcat-doc
Documentation for pxcjkcat

%package -n texlive-presentations-en-doc
Summary:        Documentation for presentations-en
Version:        svn29803.0

Provides:       tex-presentations-en-doc
AutoReqProv:    No

%description -n texlive-presentations-en-doc
Documentation for presentations-en

%package -n texlive-presentations-doc
Summary:        Documentation for presentations
Version:        svn43949
Provides:       tex-presentations-doc
AutoReqProv:    No

%description -n texlive-presentations-doc
Documentation for presentations

%package -n texlive-przechlewski-book
Provides:       tex-przechlewski-book = %{tl_version}
License:        LPPL
Summary:        Examples from Przechlewski's LaTeX book
Version:        svn23552.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(caption.sty), tex(polski.sty), tex(prelim2e.sty)
Provides:       tex(upmgr.cls) = %{tl_version}, tex(wkmgr.cls) = %{tl_version}

%description -n texlive-przechlewski-book
The bundle provides machine-readable copies of the examples
from the book "Praca magisterska i dyplomowa z programem
LaTeX".

%package -n texlive-przechlewski-book-doc
Summary:        Documentation for przechlewski-book
Version:        svn23552.0

Provides:       tex-przechlewski-book-doc
AutoReqProv:    No

%description -n texlive-przechlewski-book-doc
Documentation for przechlewski-book

%package -n texlive-psfrag
Provides:       tex-psfrag = %{tl_version}
License:        psfrag
Summary:        Replace strings in encapsulated PostScript figures
Version:        svn15878.3.04

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphics.sty)
Provides:       tex(psfrag.sty) = %{tl_version}

%description -n texlive-psfrag
Allows LaTeX constructions (equations, picture environments,
etc.) to be precisely superimposed over Encapsulated PostScript
figures, using your own favorite drawing tool to create an EPS
figure and placing simple text 'tags' where each replacement is
to be placed, with PSfrag automatically removing these tags
from the figure and replacing them with a user specified LaTeX
construction, properly aligned, scaled, and/or rotated.

%package -n texlive-psfrag-doc
Summary:        Documentation for psfrag
Version:        svn15878.3.04

Provides:       tex-psfrag-doc
AutoReqProv:    No

%description -n texlive-psfrag-doc
Documentation for psfrag

%package -n texlive-psfrag-italian-doc
Summary:        Documentation for psfrag-italian
Version:        svn15878.0

Provides:       tex-psfrag-italian-doc
AutoReqProv:    No

%description -n texlive-psfrag-italian-doc
Documentation for psfrag-italian

%package -n texlive-pxjahyper
Provides:       tex-pxjahyper = %{tl_version}
License:        MIT
Summary:        Hyperref support for pLaTeX
Version:        svn48207
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(atbegshi.sty)
Provides:       tex(pxjahyper.sty) = %{tl_version}

%description -n texlive-pxjahyper
pxjahyper package

%package -n texlive-pxjahyper-doc
Summary:        Documentation for pxjahyper
Version:        svn48207
Provides:       tex-pxjahyper-doc
AutoReqProv:    No

%description -n texlive-pxjahyper-doc
Documentation for pxjahyper

%package -n texlive-pxrubrica
Provides:       tex-pxrubrica = %{tl_version}
License:        LPPL
Summary:        pxrubrica package
Version:        svn45854
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(pxrubrica.sty) = %{tl_version}

%description -n texlive-pxrubrica
pxrubrica package

%package -n texlive-pxrubrica-doc
Summary:        Documentation for pxrubrica
Version:        svn45854
Provides:       tex-pxrubrica-doc
AutoReqProv:    No

%description -n texlive-pxrubrica-doc
Documentation for pxrubrica

%package -n texlive-prerex
Provides:       tex-prerex = %{tl_version}
License:        GPL+
Summary:        Interactive editor and macro support for prerequisite charts
Version:        svn45940
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(relsize.sty), tex(calc.sty), tex(pgf.sty), tex(tikz.sty)
Requires:       tex(textcomp.sty), tex(hyperref.sty), tex(xcolor.sty)
Provides:       tex(prerex.sty) = %{tl_version}

%description -n texlive-prerex
This package consists of prerex.sty, a LaTeX package for
producing charts of course nodes linked by arrows representing
pre- and co-requisites, and prerex, an interactive program for
creating and editing chart descriptions. The implementation of
prerex.sty uses PGF, so that it may be used equally happily
with LaTeX or pdfLaTeX; prerex itself is written in C. The
package includes source code for a previewer application, a
lightweight Qt-4 and poppler-based prerex-enabled PDF viewer.

%package -n texlive-prerex-doc
Summary:        Documentation for prerex
Version:        svn45940
Provides:       tex-prerex-doc
AutoReqProv:    No

%description -n texlive-prerex-doc
Documentation for prerex

%package -n texlive-productbox
Provides:       tex-productbox = %{tl_version}
License:        Copyright only
Summary:        Typeset a three-dimensional product box
Version:        svn20886.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty), tex(tikz.sty)
Provides:       tex(productbox.sty) = %{tl_version}

%description -n texlive-productbox
The package enables typesetting of a three-dimensional product
box. This product box can be rendered as it is standing on a
surface and some light is shed onto it. Alternatively it can be
typeset as a wireframe to be cut out and glued together. This
will lead to a physical product box. The package requires pgf
and TikZ.

%package -n texlive-productbox-doc
Summary:        Documentation for productbox
Version:        svn20886.1.1

Provides:       tex-productbox-doc
AutoReqProv:    No

%description -n texlive-productbox-doc
Documentation for productbox

%package -n texlive-pxpgfmark
Provides:       tex-pxpgfmark = %{tl_version}
License:        MIT
Summary:        e-pTeX driver for PGF inter-picture connections
Version:        svn30212.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pxpgfmark.sty) = %{tl_version}

%description -n texlive-pxpgfmark
The distributed drivers do not support the PGF feature of
"inter-picture connections" under e-pTeX and dvipdfmx. The
package uses existing features of dvipdfmx to fix this problem

%package -n texlive-pxpgfmark-doc
Summary:        Documentation for pxpgfmark
Version:        svn30212.0.2

Provides:       tex-pxpgfmark-doc
AutoReqProv:    No

%description -n texlive-pxpgfmark-doc
Documentation for pxpgfmark

%package -n texlive-preprint
Provides:       tex-preprint = %{tl_version}
License:        Public Domain
Summary:        A bundle of packages provided "as is"
Version:        svn30447.2011

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(authblk.sty) = %{tl_version}, tex(balance.sty) = %{tl_version}
Provides:       tex(figcaps.sty) = %{tl_version}, tex(fullpage.sty) = %{tl_version}
Provides:       tex(sublabel.sty) = %{tl_version}

%description -n texlive-preprint
The bundle comprises: authblk, which permits footnote style
author/affiliation input in the \author command, balance, to
balance the end of \twocolumn pages, figcaps, to send figure
captions, etc., to end document, fullpage, to set narrow page
margins and set a fixed page style, and sublabel, which permits
counters to be subnumbered.

%package -n texlive-preprint-doc
Summary:        Documentation for preprint
Version:        svn30447.2011

Provides:       tex-preprint-doc
AutoReqProv:    No

%description -n texlive-preprint-doc
Documentation for preprint

%package -n texlive-pressrelease
Provides:       tex-pressrelease = %{tl_version}
License:        LPPL 1.3
Summary:        A class for typesetting press releases
Version:        svn35147.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(marvosym.sty), tex(tikz.sty), tex(xkeyval.sty), tex(etoolbox.sty)
Requires:       tex(setspace.sty), tex(geometry.sty), tex(url.sty), tex(refcount.sty)
Provides:       tex(pressrelease-symbols.sty) = %{tl_version}
Provides:       tex(pressrelease.cls) = %{tl_version}

%description -n texlive-pressrelease
A configurable class for writing press releases.

%package -n texlive-pressrelease-doc
Summary:        Documentation for pressrelease
Version:        svn35147.1.0

Provides:       tex-pressrelease-doc
AutoReqProv:    No

%description -n texlive-pressrelease-doc
Documentation for pressrelease

%package -n texlive-prettyref
Provides:       tex-prettyref = %{tl_version}
License:        Public Domain
Summary:        Make label references "self-identify"
Version:        svn15878.3.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(prettyref.sty) = %{tl_version}

%description -n texlive-prettyref
Prettyref provides a command \newrefformat, which specifies the
way in which a reference is typeset, according to a label
"identification". The identification is set in the \label
command, by using prefixed label names; so instead of
\label{mysection}, one uses \label{sec:mysection}, and
prettyref interprets the "sec:" part. The package is compatible
with hyperref and with other packages.

%package -n texlive-prettyref-doc
Summary:        Documentation for prettyref
Version:        svn15878.3.0

Provides:       tex-prettyref-doc
AutoReqProv:    No

%description -n texlive-prettyref-doc
Documentation for prettyref

%package -n texlive-printlen
Provides:       tex-printlen = %{tl_version}
License:        LPPL
Summary:        Print lengths using specified units
Version:        svn19847.1.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(printlen.sty) = %{tl_version}

%description -n texlive-printlen
\printlength{length} prints the value of a LaTeX length in the
units specified by \uselengthunit{unit} ('unit' may be any TeX
length unit except for scaled point, viz., any of: pt, pc, in,
mm, cm, bp, dd or cc). When the unit is pt, the printed length
value will include any stretch or shrink; otherwise these are
not printed. The 'unit' argument may also be PT, in which case
length values will be printed in point units but without any
stretch or shrink values.

%package -n texlive-printlen-doc
Summary:        Documentation for printlen
Version:        svn19847.1.1a

Provides:       tex-printlen-doc
AutoReqProv:    No

%description -n texlive-printlen-doc
Documentation for printlen

%package -n texlive-probsoln
Provides:       tex-probsoln = %{tl_version}
License:        LPPL
Summary:        Generate problem sheets and their solution sheets
Version:        svn44783
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(amsmath.sty), tex(etoolbox.sty), tex(xkeyval.sty)
Provides:       tex(probsoln.sty) = %{tl_version}

%description -n texlive-probsoln
The package is designed for lecturers who have to generate new
problem sheets for their students on a regular basis (e.g.
yearly) by randomly selecting a specified number of problems
defined in another file. The package allows you easily to
generate a new problem sheet that is different from the
previous year, thus alleviating the temptation of students to
seek out the previous year's students and checking out their
answers. The solutions to the problems can be defined along
with the problem, making it easy to generate the solution sheet
from the same source code; problems may be reused within a
document, so that solutions may appear in a different section
of the same document as the problems they cover.

%package -n texlive-probsoln-doc
Summary:        Documentation for probsoln
Version:        svn44783
Provides:       tex-probsoln-doc
AutoReqProv:    No

%description -n texlive-probsoln-doc
Documentation for probsoln

%package -n texlive-program
Provides:       tex-program = %{tl_version}
License:        GPLv3+
Summary:        Typesetting programs and algorithms
Version:        svn44214
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(program.sty) = %{tl_version}

%description -n texlive-program
The main offering is a program environment; a programbox
environment is available for fragments that must not break with
the pages.

%package -n texlive-program-doc
Summary:        Documentation for program
Version:        svn44214
Provides:       tex-program-doc
AutoReqProv:    No

%description -n texlive-program-doc
Documentation for program

%package -n texlive-progress
Provides:       tex-progress = %{tl_version}
License:        LPPL
Summary:        Creates an overview of a document's state
Version:        svn19519.1.10

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(progress.sty) = %{tl_version}

%description -n texlive-progress
Progress is a package which. when compiling TeX and LaTeX
documents, generates a HTML file showing an overview of a
document's state (of how finished it is). The report is sent to
file \ProgressReportName, which is by default the \jobname with
the date appended (but is user-modifiable).

%package -n texlive-progress-doc
Summary:        Documentation for progress
Version:        svn19519.1.10

Provides:       tex-progress-doc
AutoReqProv:    No

%description -n texlive-progress-doc
Documentation for progress

%package -n texlive-progressbar
Provides:       tex-progressbar = %{tl_version}
License:        LPPL
Summary:        Visualize shares of total amounts in the form of a (progress-)bar
Version:        svn33822.v1.0b_4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(tikz.sty), tex(kvoptions.sty), tex(kvsetkeys.sty)
Provides:       tex(progressbar.sty) = %{tl_version}

%description -n texlive-progressbar
This package allows you to easily visualize shares of total
amounts in the form of a bar. So basically you can convert any
number between 0 and 1 to a progressbar using the command
\progressbar{<number>}. Also a lot of customizations are
possible, allowing you to create an unique progressbar on your
own. The package uses TikZ to produce its graphics.

%package -n texlive-progressbar-doc
Summary:        Documentation for progressbar
Version:        svn33822.v1.0b_4

Provides:       tex-progressbar-doc
AutoReqProv:    No

%description -n texlive-progressbar-doc
Documentation for progressbar

%package -n texlive-proofread
Provides:       tex-proofread = %{tl_version}
License:        LPPL 1.3
Summary:        Commands for inserting annotations
Version:        svn48322
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(soul.sty), tex(tikz.sty), tex(etoolbox.sty)
Provides:       tex(proofread.sty) = %{tl_version}

%description -n texlive-proofread
The proofread package defines a few LaTeX commands that are
useful when you proofread a LaTeX document. These allow you to
easily highlight text and add comments in the margin. Vim
escape sequences are provided for inserting these LaTeX
commands in the source. The package is based on code for a text
highlighting command that was published by Antal S-Z in
href='http://tex.stackexchange.com/questions/5959'. The main
file, proofread.dtx, is self-extracting, so you can generate
the style file by compiling proofread.dtx with pdfLaTeX.

%package -n texlive-proofread-doc
Summary:        Documentation for proofread
Version:        svn48322
Provides:       tex-proofread-doc
AutoReqProv:    No

%description -n texlive-proofread-doc
Documentation for proofread

%package -n texlive-properties
Provides:       tex-properties = %{tl_version}
License:        LPPL
Summary:        Load properties from a file
Version:        svn15878.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(datatool.sty)
Provides:       tex(properties.sty) = %{tl_version}

%description -n texlive-properties
The package loads properties (key, value) from a properties
file, e.g. \jobname.properties.

%package -n texlive-properties-doc
Summary:        Documentation for properties
Version:        svn15878.0.2

Provides:       tex-properties-doc
AutoReqProv:    No

%description -n texlive-properties-doc
Documentation for properties

%package -n texlive-prosper
Provides:       tex-prosper = %{tl_version}
License:        LPPL 1.2
Summary:        LaTeX class for high quality slides
Version:        svn33033.1.0h

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amssymb.sty), tex(pst-grad.sty), tex(semhelv.sty), tex(times.sty)
Requires:       tex(palatino.sty), tex(mathpazo.sty), tex(pst-slpe.sty), tex(multido.sty)
Requires:       tex(ifthen.sty), tex(fp.sty), tex(graphicx.sty), tex(hyperref.sty)
Provides:       tex(PPRalcatel.sty) = %{tl_version}, tex(PPRalienglow.sty) = %{tl_version}
Provides:       tex(PPRautumn.sty) = %{tl_version}, tex(PPRazure.sty) = %{tl_version}
Provides:       tex(PPRblends.sty) = %{tl_version}, tex(PPRcapsules.sty) = %{tl_version}
Provides:       tex(PPRcontemporain.sty) = %{tl_version}
Provides:       tex(PPRcorners.sty) = %{tl_version}, tex(PPRdarkblue.sty) = %{tl_version}
Provides:       tex(PPRdefault.sty) = %{tl_version}, tex(PPRframes.sty) = %{tl_version}
Provides:       tex(PPRfyma.sty) = %{tl_version}, tex(PPRgyom.sty) = %{tl_version}
Provides:       tex(PPRlignesbleues.sty) = %{tl_version}
Provides:       tex(PPRmancini.sty) = %{tl_version}, tex(PPRnuancegris.sty) = %{tl_version}
Provides:       tex(PPRprettybox.sty) = %{tl_version}, tex(PPRrico.sty) = %{tl_version}
Provides:       tex(PPRserpaggi.sty) = %{tl_version}, tex(PPRthomasd.sty) = %{tl_version}
Provides:       tex(PPRtroispoints.sty) = %{tl_version}, tex(PPRwhitecross.sty) = %{tl_version}
Provides:       tex(PPRwinter.sty) = %{tl_version}, tex(PPRwj.sty) = %{tl_version}
Provides:       tex(prosper.cls) = %{tl_version}, tetex-prosper = %{tl_version}
Obsoletes:      tetex-prosper < %{tl_version}

%description -n texlive-prosper
Prosper is a LaTeX class for writing transparencies. It is
written as an extension of the seminar class by Timothy Van
Zandt. Prosper offers a friendly environment for creating
slides for both presentations with an overhead projector and a
video projector. Slides prepared for a presentation with a
computer and a video projector may integrate animation effects,
incremental display, and so on. Various visual styles are
supported (including some that mimic PowerPoint) and others are
being contributed.

%package -n texlive-prosper-doc
Summary:        Documentation for prosper
Version:        svn33033.1.0h

Provides:       tex-prosper-doc
AutoReqProv:    No

%description -n texlive-prosper-doc
Documentation for prosper

%package -n texlive-protex
Provides:       tex-protex = %{tl_version}
License:        LPPL
Summary:        Literate programming package
Version:        svn41633
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(AlProTex.sty) = %{tl_version}, tex(ProTex.sty) = %{tl_version}

%description -n texlive-protex
ProTeX is a simple but powerful literate programming tool,
which is designed to generate useful hypertext output (either
PDF, or HTML using TeX4ht).

%package -n texlive-protex-doc
Summary:        Documentation for protex
Version:        svn41633
Provides:       tex-protex-doc
AutoReqProv:    No

%description -n texlive-protex-doc
Documentation for protex

%package -n texlive-protocol
Provides:       tex-protocol = %{tl_version}
License:        LPPL 1.3
Summary:        A class for minutes of meetings
Version:        svn25562.1.13

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(protocol.cls) = %{tl_version}

%description -n texlive-protocol
The present version of the class supports German meeting
minutes including vote results and action items. The author has
ambitions to internationalise the code, and would welcome
support in the work.

%package -n texlive-protocol-doc
Summary:        Documentation for protocol
Version:        svn25562.1.13

Provides:       tex-protocol-doc
AutoReqProv:    No

%description -n texlive-protocol-doc
Documentation for protocol

%package -n texlive-psfragx
Provides:       tex-psfragx = %{tl_version}
License:        LPPL
Summary:        A psfrag eXtension
Version:        svn26243.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(psfrag.sty), tex(overpic.sty)
Provides:       tex(psfragx.cfg) = %{tl_version}, tex(psfragx.sty) = %{tl_version}

%description -n texlive-psfragx
PSfragX offers a mechanism to embed \psfrag commands, as
provided by the psfrag package, into the EPS file itself. Each
time a graphic is included, the EPS file is scanned. If some
tagged lines are found, they are used to define the psfrag
replacements that should be performed automatically. In
addition, a similar mechanism holds for overpic objects. These
are picture objects superimposed on the included graphic. A
similar mechanism is implemented in psfrag itself (but
deprecated in the documentation), but psfragx offers much more
flexibility. For example, if babel is used, it is possible to
define different replacements corresponding to different
languages. The replacements to take into account will be
selected on the basis of the current language of the document.
A Matlab script (LaPrint) is provided, to export an EPS file
with psfragx annotations ready embedded.

%package -n texlive-psfragx-doc
Summary:        Documentation for psfragx
Version:        svn26243.1.1

Provides:       tex-psfragx-doc
AutoReqProv:    No

%description -n texlive-psfragx-doc
Documentation for psfragx

%package -n texlive-pstool
Provides:       tex-pstool = %{tl_version}
License:        LPPL
Summary:        Support for psfrag within pdfLaTeX
Version:        svn46393
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(catchfile.sty), tex(color.sty), tex(ifpdf.sty), tex(ifplatform.sty)
Requires:       tex(filemod.sty), tex(graphicx.sty), tex(psfrag.sty), tex(suffix.sty)
Requires:       tex(trimspaces.sty), tex(xkeyval.sty), tex(expl3.sty)
Provides:       tex(pstool.sty) = %{tl_version}

%description -n texlive-pstool
The package works in the same sort of way as pst-pdf, but it
also processes the PostScript graphics with psfrag to add
labels within the graphic, before conversion. Thus the bundle
replaces two steps of an ordinary workflow. (Naturally, the
package requires that \write 18 is enabled.) Pstool ensures
that each version of each graphic is compiled once only (the
graphic is (re-)compiled only if it has changed since the
previous compilation of the document). This drastically speeds
up the running of the package in the typical case (though the
first run of any document is inevitably just as slow as with
any similar package).

%package -n texlive-pstool-doc
Summary:        Documentation for pstool
Version:        svn46393
Provides:       tex-pstool-doc
AutoReqProv:    No

%description -n texlive-pstool-doc
Documentation for pstool

%package -n texlive-pxgreeks
Provides:       tex-pxgreeks = %{tl_version}
License:        LPPL 1.3
Summary:        Shape selection for PX fonts Greek letters
Version:        svn21838.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pxfonts.sty)
Provides:       tex(pxgreeks.sty) = %{tl_version}

%description -n texlive-pxgreeks
The package allows LaTeX maths users of the PX fonts to select
the shapes (italic or upright) for the Greek lowercase and
uppercase letters. Once the shapes for lowercase and uppercase
have been selected via a package option, the \other prefix
(e.g., \otheralpha) allows using the alternate glyph (as in the
fourier package). The pxgreeks package does not constrain the
text font that may be used in the document.

%package -n texlive-pxgreeks-doc
Summary:        Documentation for pxgreeks
Version:        svn21838.1.0

Provides:       tex-pxgreeks-doc
AutoReqProv:    No

%description -n texlive-pxgreeks-doc
Documentation for pxgreeks

%package -n texlive-python
Provides:       tex-python = %{tl_version}
License:        GPL+
Summary:        Embed Python code in LaTeX
Version:        svn27064.0.21

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(python.sty) = %{tl_version}

%description -n texlive-python
The package enables you to embed Python code in LaTeX, and
insert the script's output in the document.

%package -n texlive-python-doc
Summary:        Documentation for python
Version:        svn27064.0.21

Provides:       tex-python-doc
AutoReqProv:    No

%description -n texlive-python-doc
Documentation for python

%package -n texlive-prftree
Provides:       tex-prftree = %{tl_version}
License:        GPL+
Summary:        Macros for building proof trees
Version:        svn41985
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(prftree.sty) = %{tl_version}

%description -n texlive-prftree
A package to typeset proof trees for natural deduction calculi,
sequent-like calculi, and similar.

%package -n texlive-prftree-doc
Summary:        Documentation for prftree
Version:        svn41985
Provides:       tex-prftree-doc
AutoReqProv:    No

%description -n texlive-prftree-doc
Documentation for prftree

%package -n texlive-proba
Provides:       tex-proba = %{tl_version}
License:        LPPL
Summary:        Shortcuts commands to symbols used in probability texts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsfonts.sty)
Provides:       tex(proba.sty) = %{tl_version}

%description -n texlive-proba
This package includes some of the most often used commands in
probability texts, e.g. probability, expectation, variance,
etc. It also includes some short commands for set (blackboard)
or filtrations (calligraphic). It requires LaTeX2e and the
amsfonts package.

%package -n texlive-proba-doc
Summary:        Documentation for proba
Version:        svn15878.0

Provides:       tex-proba-doc
AutoReqProv:    No

%description -n texlive-proba-doc
Documentation for proba

%package -n texlive-present
Provides:       tex-present = %{tl_version}
License:        LPPL
Summary:        Presentations with Plain TeX
Version:        svn25953.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(present.tex) = %{tl_version}

%description -n texlive-present
The package offers a collection of simple macros for preparing
presentations in Plain TeX. Slide colour and text colour may be
set, links between parts of the presentation, to other files,
and to web addresses may be inserted. Images may be included
easily, and code is available to provide transition effects
between slides or frames. The structure of the macros is not
overly complex, so that users should find it easy to adapt the
macros to their specific needs.

%package -n texlive-present-doc
Summary:        Documentation for present
Version:        svn25953.2.2

Provides:       tex-present-doc
AutoReqProv:    No

%description -n texlive-present-doc
Documentation for present

%package -n texlive-psbao
Provides:       tex-psbao = %{tl_version}
License:        LPPL
Summary:        Draw Bao diagrams
Version:        svn15878.0.17

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(calc.sty), tex(ifthen.sty), tex(cool.sty)
Requires:       tex(etex.sty)
Provides:       tex(psbao.sty) = %{tl_version}

%description -n texlive-psbao
The package draws Bao diagrams in LaTeX. The package is a
development of psgo, and uses PSTricks to draw the diagrams.

%package -n texlive-psbao-doc
Summary:        Documentation for psbao
Version:        svn15878.0.17

Provides:       tex-psbao-doc
AutoReqProv:    No

%description -n texlive-psbao-doc
Documentation for psbao

%package -n texlive-pst-2dplot
Provides:       tex-pst-2dplot = %{tl_version}
License:        LPPL
Summary:        A PSTricks package for drawing 2D curves
Version:        svn15878.1.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pst-2dplot.sty) = %{tl_version}

%description -n texlive-pst-2dplot
Pst-2dplot is a pstricks package that offers an easy-to-use and
intuitive tool for plotting 2-d curves. It defines an
environment with commands similar to MATLAB for plotting.

%package -n texlive-pst-2dplot-doc
Summary:        Documentation for pst-2dplot
Version:        svn15878.1.5

Provides:       tex-pst-2dplot-doc
AutoReqProv:    No

%description -n texlive-pst-2dplot-doc
Documentation for pst-2dplot

%package -n texlive-pst-3d
Provides:       tex-pst-3d = %{tl_version}
License:        LPPL
Summary:        A PSTricks package for tilting and other pseudo-3D tricks
Version:        svn17257.1.10

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-3d.tex) = %{tl_version}, tex(pst-3d.sty) = %{tl_version}

%description -n texlive-pst-3d
The package provides basic macros that use PSTricks for
shadows, tilting and three dimensional representations of text
or graphical objects.

%package -n texlive-pst-3d-doc
Summary:        Documentation for pst-3d
Version:        svn17257.1.10

Provides:       tex-pst-3d-doc
AutoReqProv:    No

%description -n texlive-pst-3d-doc
Documentation for pst-3d

%package -n texlive-pst-3dplot
Provides:       tex-pst-3dplot = %{tl_version}
License:        LPPL
Summary:        Draw 3D objects in parallel projection, using PSTricks
Version:        svn43703
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty), tex(pst-3d.sty), tex(pst-plot.sty), tex(pst-node.sty)
Requires:       tex(multido.sty)
Provides:       tex(pst-3dplot.tex) = %{tl_version}, tex(pst-3dplot.sty) = %{tl_version}

%description -n texlive-pst-3dplot
A package using PSTricks to draw a large variety of graphs and
plots, including 3D maths functions. Data can be read from
external data files, making this package a generic tool for
graphing within TeX/LaTeX, without the need for external tools.

%package -n texlive-pst-3dplot-doc
Summary:        Documentation for pst-3dplot
Version:        svn43703
Provides:       tex-pst-3dplot-doc
AutoReqProv:    No

%description -n texlive-pst-3dplot-doc
Documentation for pst-3dplot

%package -n texlive-pst-abspos
Provides:       tex-pst-abspos = %{tl_version}
License:        LPPL
Summary:        Put objects at an absolute position
Version:        svn15878.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-abspos.tex) = %{tl_version}, tex(pst-abspos.sty) = %{tl_version}

%description -n texlive-pst-abspos
The (PSTricks-related) package provides a command
\pstPutAbs(x,y) to put an object at an arbitrary absolute (or
even a relative) position on the page.

%package -n texlive-pst-abspos-doc
Summary:        Documentation for pst-abspos
Version:        svn15878.0.2

Provides:       tex-pst-abspos-doc
AutoReqProv:    No

%description -n texlive-pst-abspos-doc
Documentation for pst-abspos

%package -n texlive-pst-am
Provides:       tex-pst-am = %{tl_version}
License:        LPPL
Summary:        Simulation of modulation and demodulation
Version:        svn19591.1.02

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(pst-plot.sty), tex(pst-node.sty), tex(pst-xkey.sty)
Requires:       tex(numprint.sty), tex(multido.sty)
Provides:       tex(pst-am.sty) = %{tl_version}

%description -n texlive-pst-am
The package allows the simulation of the modulated and
demodulated amplitude of radio waves. The user may plot curves
of modulated signals, wave carrier, signal modulation, signal
recovery and signal demodulation.

%package -n texlive-pst-am-doc
Summary:        Documentation for pst-am
Version:        svn19591.1.02

Provides:       tex-pst-am-doc
AutoReqProv:    No

%description -n texlive-pst-am-doc
Documentation for pst-am

%package -n texlive-pst-asr
Provides:       tex-pst-asr = %{tl_version}
License:        LPPL
Summary:        Typeset autosegmental representations for linguists
Version:        svn22138.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(pst-xkey.sty)
Provides:       tex(pst-asr.tex) = %{tl_version}, tex(pst-asr.sty) = %{tl_version}

%description -n texlive-pst-asr
The package allows the user to typeset autosegmental
representations. It uses the PStricks, and xkeyval packages.

%package -n texlive-pst-asr-doc
Summary:        Documentation for pst-asr
Version:        svn22138.1.3

Provides:       tex-pst-asr-doc
AutoReqProv:    No

%description -n texlive-pst-asr-doc
Documentation for pst-asr

%package -n texlive-pst-bar
Provides:       tex-pst-bar = %{tl_version}
License:        LPPL
Summary:        Produces bar charts using pstricks
Version:        svn18734.0.92

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-bar.tex) = %{tl_version}, tex(pst-bar.sty) = %{tl_version}

%description -n texlive-pst-bar
The package uses pstricks to draw bar charts from data stored
in a comma-delimited file. Several types of bar charts may be
drawn, and the drawing parameters are highly customizable. No
external packages are required except those that are part of
the standard pstricks distribution.

%package -n texlive-pst-bar-doc
Summary:        Documentation for pst-bar
Version:        svn18734.0.92

Provides:       tex-pst-bar-doc
AutoReqProv:    No

%description -n texlive-pst-bar-doc
Documentation for pst-bar

%package -n texlive-pst-barcode
Provides:       tex-pst-barcode = %{tl_version}
License:        LPPL
Summary:        Print barcodes using PostScript
Version:        svn45096
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-barcode.tex) = %{tl_version}, tex(pst-barcode.sty) = %{tl_version}

%description -n texlive-pst-barcode
The pst-barcode package allows printing of barcodes, in a huge
variety of formats, including quick-response (qr) codes (see
documentation for details). As a pstricks package, the package
requires pstricks. The package uses PostScript for calculating
the bars. For PDF output use a multi-pass mechansism such as
pst-pdf.

%package -n texlive-pst-barcode-doc
Summary:        Documentation for pst-barcode
Version:        svn45096
Provides:       tex-pst-barcode-doc
AutoReqProv:    No

%description -n texlive-pst-barcode-doc
Documentation for pst-barcode

%package -n texlive-pst-bezier
Provides:       tex-pst-bezier = %{tl_version}
License:        LPPL
Summary:        Draw Bezier curves
Version:        svn41981
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-bezier.tex) = %{tl_version}, tex(pst-bezier.sty) = %{tl_version}

%description -n texlive-pst-bezier
The package provides a macro \psbcurve for drawing a Bezier
curve. Provision is made for full control of over all the
control points of the curve.

%package -n texlive-pst-bezier-doc
Summary:        Documentation for pst-bezier
Version:        svn41981
Provides:       tex-pst-bezier-doc
AutoReqProv:    No

%description -n texlive-pst-bezier-doc
Documentation for pst-bezier

%package -n texlive-pst-blur
Provides:       tex-pst-blur = %{tl_version}
License:        LPPL
Summary:        PSTricks package for "blurred" shadows
Version:        svn15878.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-blur.tex) = %{tl_version}, tex(pst-blur.sty) = %{tl_version}

%description -n texlive-pst-blur
Pst-blur is a package built for use with PSTricks. It provides
macros that apply blurring to the normal shadow function of
PSTricks.

%package -n texlive-pst-blur-doc
Summary:        Documentation for pst-blur
Version:        svn15878.2.0

Provides:       tex-pst-blur-doc
AutoReqProv:    No

%description -n texlive-pst-blur-doc
Documentation for pst-blur

%package -n texlive-pst-bspline
Provides:       tex-pst-bspline = %{tl_version}
License:        LPPL
Summary:        Draw cubic Bspline curves and interpolations
Version:        svn40685

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pst-bspline.tex) = %{tl_version}, tex(pst-bspline.sty) = %{tl_version}

%description -n texlive-pst-bspline
The package draws uniform, cubic B-spline curves, open and
closed, based on a sequence of B-spline control points. There
is also code which permits drawing the open or closed cubic
Bspline curve interpolating a sequence of points. Graphical
output is created using PStricks.

%package -n texlive-pst-bspline-doc
Summary:        Documentation for pst-bspline
Version:        svn40685

Provides:       tex-pst-bspline-doc
AutoReqProv:    No

%description -n texlive-pst-bspline-doc
Documentation for pst-bspline

%package -n texlive-pst-calendar
Provides:       tex-pst-calendar = %{tl_version}
License:        LPPL
Summary:        Plot calendars in "fancy" ways
Version:        svn15878.0.47

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fp.sty), tex(pstricks.sty), tex(pst-3d.sty), tex(multido.sty)
Requires:       tex(pst-xkey.sty)
Provides:       tex(pst-calendar.sty) = %{tl_version}

%description -n texlive-pst-calendar
The package uses pstricks and pst-3d to draw tabular calendars,
or calendars on dodecahedra with a month to each face (the
package also requires the multido and pst-xkey packages). The
package works for years 2000-2099, and has options for
calendars in French German and English, but the documentation
is not available in English.

%package -n texlive-pst-calendar-doc
Summary:        Documentation for pst-calendar
Version:        svn15878.0.47

Provides:       tex-pst-calendar-doc
AutoReqProv:    No

%description -n texlive-pst-calendar-doc
Documentation for pst-calendar

%package -n texlive-pst-circ
Provides:       tex-pst-circ = %{tl_version}
License:        LPPL
Summary:        PSTricks package for drawing electric circuits
Version:        svn45829
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-circ.tex) = %{tl_version}, tex(pst-circ.sty) = %{tl_version}

%description -n texlive-pst-circ
The package is built using PSTricks and in particular pst-node.
It can easily draw current 2-terminal devices and some 3- and 4-
terminal devices used in electronic or electric theory. The
package's macros are designed with a view to 'logical'
representation of circuits, as far as possible, so as to
relieve the user of purely graphical considerations when
expressing a circuit.

%package -n texlive-pst-circ-doc
Summary:        Documentation for pst-circ
Version:        svn45829
Provides:       tex-pst-circ-doc
AutoReqProv:    No

%description -n texlive-pst-circ-doc
Documentation for pst-circ

%package -n texlive-pst-coil
Provides:       tex-pst-coil = %{tl_version}
License:        LPPL
Summary:        A PSTricks package for coils, etc
Version:        svn37377.1.07

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-coil.tex) = %{tl_version}, tex(pst-coil.sty) = %{tl_version}

%description -n texlive-pst-coil
Pst-coil is a PSTricks based package for coils and zigzags and
for coil and zigzag node connections.

%package -n texlive-pst-coil-doc
Summary:        Documentation for pst-coil
Version:        svn37377.1.07

Provides:       tex-pst-coil-doc
AutoReqProv:    No

%description -n texlive-pst-coil-doc
Documentation for pst-coil

%package -n texlive-pst-cox
Provides:       tex-pst-cox = %{tl_version}
License:        LGPLv2+
Summary:        Drawing regular complex polytopes with PSTricks
Version:        svn15878.0.98_Beta

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-coxcoor.tex) = %{tl_version}, tex(pst-coxeterp.tex) = %{tl_version}
Provides:       tex(pst-coxcoor.sty) = %{tl_version}, tex(pst-coxeterp.sty) = %{tl_version}

%description -n texlive-pst-cox
Pst-cox is a PSTricks package for drawing 2-dimensional
projections of complex regular polytopes (after the work of
Coxeter). The package consists of a macro library for drawing
the projections. The complex polytopes appear in the study of
the root systems and play a crucial role in many domains
related to mathematics and physics. These polytopes have been
completely described by Coxeter in his book "Regular Complex
Polytopes". There exist only a finite numbers of exceptional
regular complex polytopes (for example the icosahedron) and
some infinite series (for example, one can construct a multi-
dimensional analogue of the hypercube in any finite dimension).
The library contains two packages. The first, pst-coxcoor, is
devoted to the exceptional complex regular polytopes whose
coordinates have been pre-computed. The second, pst-coxeterp,
is devoted to the infinite series.

%package -n texlive-pst-cox-doc
Summary:        Documentation for pst-cox
Version:        svn15878.0.98_Beta

Provides:       tex-pst-cox-doc
AutoReqProv:    No

%description -n texlive-pst-cox-doc
Documentation for pst-cox

%package -n texlive-pst-dbicons
Provides:       tex-pst-dbicons = %{tl_version}
License:        LPPL
Summary:        Support for drawing ER diagrams
Version:        svn17556.0.16

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pst-dbicons.sty) = %{tl_version}

%description -n texlive-pst-dbicons
The package provides some useful macros in the database area.
The package focusses on typesetting ER-Diagrams in a
declarative style, i.e., by positioning some nodes and defining
the position of all other nodes relative to them by using the
standard database terminology. The PSTricks package is required
for using pst-dbicons, but no deep knowledge of PSTricks
commands is required (although such knowledge is useful for
exploiting the full functionality of the package).

%package -n texlive-pst-dbicons-doc
Summary:        Documentation for pst-dbicons
Version:        svn17556.0.16

Provides:       tex-pst-dbicons-doc
AutoReqProv:    No

%description -n texlive-pst-dbicons-doc
Documentation for pst-dbicons

%package -n texlive-pst-diffraction
Provides:       tex-pst-diffraction = %{tl_version}
License:        LPPL
Summary:        Print diffraction patterns from various apertures
Version:        svn15878.2.03

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(pst-3dplot.sty), tex(pst-xkey.sty)
Provides:       tex(pst-diffraction.tex) = %{tl_version}
Provides:       tex(pst-diffraction.sty) = %{tl_version}

%description -n texlive-pst-diffraction
The package enables the user to draw (using PSTricks) the
diffraction patterns for different geometric forms of apertures
for monochromatic light (using PSTricks). The aperture stops
can have rectangular, circular or triangular openings. The view
of the diffraction may be planar, or three-dimensional. Options
available are the dimensions of the aperture under
consideration and of the particular optical setting, e.g. the
radius in case of an circular opening. Moreover one can choose
the wavelength of the light (the associated color will be
calculated by the package).

%package -n texlive-pst-diffraction-doc
Summary:        Documentation for pst-diffraction
Version:        svn15878.2.03

Provides:       tex-pst-diffraction-doc
AutoReqProv:    No

%description -n texlive-pst-diffraction-doc
Documentation for pst-diffraction

%package -n texlive-pst-electricfield
Provides:       tex-pst-electricfield = %{tl_version}
License:        LPPL
Summary:        Draw electric field and equipotential lines with PStricks
Version:        svn29803.0.14

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-electricfield.tex) = %{tl_version}
Provides:       tex(pst-electricfield.sty) = %{tl_version}

%description -n texlive-pst-electricfield
The package provides macros to plot electric field and
equipotential lines using PStricks. There may be any number of
charges which can be placed in a cartesian coordinate system by
(x,y) values.

%package -n texlive-pst-electricfield-doc
Summary:        Documentation for pst-electricfield
Version:        svn29803.0.14

Provides:       tex-pst-electricfield-doc
AutoReqProv:    No

%description -n texlive-pst-electricfield-doc
Documentation for pst-electricfield

%package -n texlive-pst-eps
Provides:       tex-pst-eps = %{tl_version}
License:        LPPL
Summary:        Create EPS files from PSTricks figures
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-eps.tex) = %{tl_version}, tex(pst-eps.sty) = %{tl_version}

%description -n texlive-pst-eps
Pst-eps is a PSTricks-based package for exporting PSTricks
images 'on the fly' to encapsulated PostScript (EPS) image
files, which can then be read into a document in the usual way.

%package -n texlive-pst-eps-doc
Summary:        Documentation for pst-eps
Version:        svn15878.1.0

Provides:       tex-pst-eps-doc
AutoReqProv:    No

%description -n texlive-pst-eps-doc
Documentation for pst-eps

%package -n texlive-pst-eucl
Provides:       tex-pst-eucl = %{tl_version}
License:        LPPL
Summary:        Euclidian geometry with pstricks
Version:        svn43911
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty), tex(pst-node.sty), tex(pst-tools.sty)
Provides:       tex(pst-eucl.tex) = %{tl_version}, tex(pst-eucl.sty) = %{tl_version}

%description -n texlive-pst-eucl
The package allows the drawing of Euclidean geometric figures
using TeX pstricks macros for specifying mathematical
constraints. It is thus possible to build point using common
transformations or intersections. The use of coordinates is
limited to points which controlled the figure.

%package -n texlive-pst-eucl-doc
Summary:        Documentation for pst-eucl
Version:        svn43911
Provides:       tex-pst-eucl-doc
AutoReqProv:    No

%description -n texlive-pst-eucl-doc
Documentation for pst-eucl

%package -n texlive-pst-exa
Provides:       tex-pst-exa = %{tl_version}
License:        LPPL
Summary:        Typeset PSTricks examples, with code
Version:        svn45289
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(etoolbox.sty), tex(xcolor.sty), tex(showexpl.sty), tex(accsupp.sty)
Requires:       tex(changepage.sty), tex(tcolorbox.sty)
Provides:       tex(pst-exa.sty) = %{tl_version}

%description -n texlive-pst-exa
The (PSTricks-related) package provides an environment
PSTexample to put code and output side by side or one above the
other.

%package -n texlive-pst-exa-doc
Summary:        Documentation for pst-exa
Version:        svn45289
Provides:       tex-pst-exa-doc
AutoReqProv:    No

%description -n texlive-pst-exa-doc
Documentation for pst-exa

%package -n texlive-pst-fill
Provides:       tex-pst-fill = %{tl_version}
License:        LPPL
Summary:        Fill or tile areas with PSTricks
Version:        svn15878.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-fill.tex) = %{tl_version}, tex(pst-fill.sty) = %{tl_version}

%description -n texlive-pst-fill
Pst-fill is a PSTricks-based package for filling and tiling
areas or characters.

%package -n texlive-pst-fill-doc
Summary:        Documentation for pst-fill
Version:        svn15878.1.01

Provides:       tex-pst-fill-doc
AutoReqProv:    No

%description -n texlive-pst-fill-doc
Documentation for pst-fill

%package -n texlive-pst-fit
Provides:       tex-pst-fit = %{tl_version}
License:        LPPL
Summary:        Macros for curve fitting
Version:        svn45109
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty), tex(pstricks-add.sty)
Provides:       tex(pst-fit.tex) = %{tl_version}, tex(pst-fit.sty) = %{tl_version}

%description -n texlive-pst-fit
The package uses PSTricks to fit curves to: Linear Functions;
Power Functions; exp Function; Log_{10} and Log_e functions;
Recip; Kings Law data; Gaussian; and 4th order Polynomial

%package -n texlive-pst-fit-doc
Summary:        Documentation for pst-fit
Version:        svn45109
Provides:       tex-pst-fit-doc
AutoReqProv:    No

%description -n texlive-pst-fit-doc
Documentation for pst-fit

%package -n texlive-pst-fr3d
Provides:       tex-pst-fr3d = %{tl_version}
License:        LPPL
Summary:        Draw 3-dimensional framed boxes using PSTricks
Version:        svn15878.1.10

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pst-fr3d.tex) = %{tl_version}, tex(pst-fr3d.sty) = %{tl_version}

%description -n texlive-pst-fr3d
A package using PSTricks to draw three dimensional framed boxes
using a macro \PstFrameBoxThreeD. The macro is especially
useful for drawing 3d-seeming buttons.

%package -n texlive-pst-fr3d-doc
Summary:        Documentation for pst-fr3d
Version:        svn15878.1.10

Provides:       tex-pst-fr3d-doc
AutoReqProv:    No

%description -n texlive-pst-fr3d-doc
Documentation for pst-fr3d

%package -n texlive-pst-fractal
Provides:       tex-pst-fractal = %{tl_version}
License:        LPPL
Summary:        Draw fractal sets using PSTricks
Version:        svn45977
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-fractal.tex) = %{tl_version}, tex(pst-fractal.sty) = %{tl_version}

%description -n texlive-pst-fractal
The package uses PSTricks to draw the Julia and Mandelbrot
sets, the Sierpinski triangle, Koch flake, and Apollonius
Circle as well as fractal trees (which need not be balanced)
with a variety of different parameters (including varying
numbers of iterations). The package uses the pst-xkey package,
part of the xkeyval distribution.

%package -n texlive-pst-fractal-doc
Summary:        Documentation for pst-fractal
Version:        svn45977
Provides:       tex-pst-fractal-doc
AutoReqProv:    No

%description -n texlive-pst-fractal-doc
Documentation for pst-fractal

%package -n texlive-pst-fun
Provides:       tex-pst-fun = %{tl_version}
License:        LPPL
Summary:        Draw "funny" objects with PSTricks
Version:        svn17909.0.04

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(pst-grad.sty), tex(pst-slpe.sty), tex(multido.sty)
Provides:       tex(pst-fun.tex) = %{tl_version}, tex(pst-fun.sty) = %{tl_version}

%description -n texlive-pst-fun
This is a PSTricks related package for drawing funny objects,
like ant, bird, fish, kangaroo, ... Such objects may be useful
for testing other PSTricks macros and/or packages. (Or they can
be used for fun...)

%package -n texlive-pst-fun-doc
Summary:        Documentation for pst-fun
Version:        svn17909.0.04

Provides:       tex-pst-fun-doc
AutoReqProv:    No

%description -n texlive-pst-fun-doc
Documentation for pst-fun

%package -n texlive-pst-func
Provides:       tex-pst-func = %{tl_version}
License:        LPPL
Summary:        PSTricks package for plotting mathematical functions
Version:        svn47400
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-func.tex) = %{tl_version}, tex(pst-func.sty) = %{tl_version}

%description -n texlive-pst-func
The package is built for use with PSTricks. It provides macros
for plotting and manipulating various mathematical functions:
polynomials and their derivatives f(x)=an*x^n+an-1*x^(n-
1)+...+a0 defined by the coefficients a0 a1 a2 ... and the
derivative order; the Fourier sum f(x) = a0/2+a1cos(omega
x)+...+b1sin(omega x)+... defined by the coefficients a0 a1 a2
... b1 b2 b3 ...; the Bessel function defined by its order; the
Gauss function defined by sigma and mu; Bezier curves from
order 1 (two control points) to order 9 (10 control points);
the superellipse function (the Lame curve); Chebyshev
polynomials of the first and second kind; the Thomae (or
popcorn) function; the Weierstrass function; various
integration-derived functions; normal, binomial, poisson,
gamma, chi-squared, student's t, F, beta, Cauchy and Weibull
distribution functions and the Lorenz curve; the zeroes of a
function, or the intermediate point of two functions; the
Vasicek function for describing the evolution of interest
rates; and implicit functions. The plots may be generated as
volumes of rotation about the X-axis, as well.

%package -n texlive-pst-func-doc
Summary:        Documentation for pst-func
Version:        svn47400
Provides:       tex-pst-func-doc
AutoReqProv:    No

%description -n texlive-pst-func-doc
Documentation for pst-func

%package -n texlive-pst-gantt
Provides:       tex-pst-gantt = %{tl_version}
License:        LPPL
Summary:        Draw GANTT charts with pstricks
Version:        svn35832.0.22a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-gantt.tex) = %{tl_version}, tex(pst-gantt.sty) = %{tl_version}

%description -n texlive-pst-gantt
The package uses PSTricks to draw GANTT charts, which are a
kind of bar chart that displays a project schedule. The package
requires the pstricks apparatus, of course.

%package -n texlive-pst-gantt-doc
Summary:        Documentation for pst-gantt
Version:        svn35832.0.22a

Provides:       tex-pst-gantt-doc
AutoReqProv:    No

%description -n texlive-pst-gantt-doc
Documentation for pst-gantt

%package -n texlive-pst-geo
Provides:       tex-pst-geo = %{tl_version}
License:        LPPL
Summary:        Geographical Projections
Version:        svn46273
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(aus.dat) = %{tl_version}, tex(c-cap.dat) = %{tl_version}
Provides:       tex(c-sub.dat) = %{tl_version}, tex(canada.dat) = %{tl_version}
Provides:       tex(capitales.tex) = %{tl_version}, tex(capitales3d.tex) = %{tl_version}
Provides:       tex(capitals.dat) = %{tl_version}, tex(cities.tex) = %{tl_version}
Provides:       tex(citycapitals.dat) = %{tl_version}, tex(citysub.dat) = %{tl_version}
Provides:       tex(corse.dat) = %{tl_version}, tex(france.dat) = %{tl_version}
Provides:       tex(mex.dat) = %{tl_version}, tex(pborder.dat) = %{tl_version}
Provides:       tex(pcoast.dat) = %{tl_version}, tex(pisland.dat) = %{tl_version}
Provides:       tex(plake.dat) = %{tl_version}, tex(rhone.dat) = %{tl_version}
Provides:       tex(ridge.dat) = %{tl_version}, tex(river.dat) = %{tl_version}
Provides:       tex(seine.dat) = %{tl_version}, tex(transfrm.dat) = %{tl_version}
Provides:       tex(trench.dat) = %{tl_version}, tex(usa.dat) = %{tl_version}
Provides:       tex(villesFrance.tex) = %{tl_version}, tex(villesFrance3d.tex) = %{tl_version}
Provides:       tex(villesItalia.tex) = %{tl_version}, tex(villesItalia3d.tex) = %{tl_version}
Provides:       tex(wfraczon.dat) = %{tl_version}, tex(wmaglin.dat) = %{tl_version}
Provides:       tex(africa-bdy.dat) = %{tl_version}, tex(africa-cil.dat) = %{tl_version}
Provides:       tex(africa-riv.dat) = %{tl_version}, tex(asia-bdy.dat) = %{tl_version}
Provides:       tex(asia-cil.dat) = %{tl_version}, tex(asia-isl.dat) = %{tl_version}
Provides:       tex(asia-riv.dat) = %{tl_version}, tex(c-cap.dat) = %{tl_version}
Provides:       tex(c-sub.dat) = %{tl_version}, tex(citycapitals.dat) = %{tl_version}
Provides:       tex(citysub.dat) = %{tl_version}, tex(europe-bdy.dat) = %{tl_version}
Provides:       tex(europe-cil.dat) = %{tl_version}, tex(europe-riv.dat) = %{tl_version}
Provides:       tex(namer-bdy.dat) = %{tl_version}, tex(namer-cil.dat) = %{tl_version}
Provides:       tex(namer-pby.dat) = %{tl_version}, tex(namer-riv.dat) = %{tl_version}
Provides:       tex(samer-arc.dat) = %{tl_version}, tex(samer-bdy.dat) = %{tl_version}
Provides:       tex(samer-cil.dat) = %{tl_version}, tex(samer-riv.dat) = %{tl_version}
Provides:       tex(pst-map2d.tex) = %{tl_version}, tex(pst-map2dII.tex) = %{tl_version}
Provides:       tex(pst-map3d.tex) = %{tl_version}, tex(pst-map3dII.tex) = %{tl_version}
Provides:       tex(pst-map2d.sty) = %{tl_version}, tex(pst-map2dII.sty) = %{tl_version}
Provides:       tex(pst-map3d.sty) = %{tl_version}, tex(pst-map3dII.sty) = %{tl_version}

%description -n texlive-pst-geo
The package offers a set of PSTricks related packages for
various cartographic projections of the terrestrial sphere. The
package pst-map2d provides conventional projections such as
Mercator, Lambert, cylindrical, etc. The package pst-map3d
treats representation in three dimensions of the terrestrial
sphere. Packages pst-map2dII and pst-map3dII allow use of the
CIA World DataBank II. Various parameters of the packages allow
for choice of the level of the detail and the layouts possible
(cities, borders, rivers etc). Substantial data files are
provided, in an (internally) compressed format. Decompression
happens on-the-fly as a document using the data is displayed,
printed or converted to PDF format. A Perl script is provided
for the user to do the decompression, if the need should arise.

%package -n texlive-pst-geo-doc
Summary:        Documentation for pst-geo
Version:        svn46273
Provides:       tex-pst-geo-doc
AutoReqProv:    No

%description -n texlive-pst-geo-doc
Documentation for pst-geo

%package -n texlive-pst-ghsb
Provides:       tex-pst-ghsb = %{tl_version}
License:        LPPL
Summary:        pst-ghsb package
Version:        svn45797
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(pst-ghsb.tex) = %{tl_version}, tex(pst-ghsb.sty) = %{tl_version}

%description -n texlive-pst-ghsb
pst-ghsb package

%package -n texlive-pst-ghsb-doc
Summary:        Documentation for pst-ghsb
Version:        svn45797
Provides:       tex-pst-ghsb-doc
AutoReqProv:    No

%description -n texlive-pst-ghsb-doc
Documentation for pst-ghsb

%package -n texlive-pst-gr3d
Provides:       tex-pst-gr3d = %{tl_version}
License:        LPPL
Summary:        Three dimensional grids with PSTricks
Version:        svn15878.1.34

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-gr3d.tex) = %{tl_version}, tex(pst-gr3d.sty) = %{tl_version}

%description -n texlive-pst-gr3d
This PSTricks package provides a command \PstGridThreeD that
will draw a three dimensional grid, offering a number of
options for its appearance.

%package -n texlive-pst-gr3d-doc
Summary:        Documentation for pst-gr3d
Version:        svn15878.1.34

Provides:       tex-pst-gr3d-doc
AutoReqProv:    No

%description -n texlive-pst-gr3d-doc
Documentation for pst-gr3d

%package -n texlive-pst-grad
Provides:       tex-pst-grad = %{tl_version}
License:        LPPL
Summary:        Filling with colour gradients, using PStricks
Version:        svn15878.1.06

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-grad.tex) = %{tl_version}, tex(pst-grad.sty) = %{tl_version}

%description -n texlive-pst-grad
The package fills with colour gradients, using PSTricks. The
RGB, CMYK and HSB models are supported. Other colour gradient
mechanisms are to be found in package pst-slpe.

%package -n texlive-pst-grad-doc
Summary:        Documentation for pst-grad
Version:        svn15878.1.06

Provides:       tex-pst-grad-doc
AutoReqProv:    No

%description -n texlive-pst-grad-doc
Documentation for pst-grad

%package -n texlive-pst-graphicx
Provides:       tex-pst-graphicx = %{tl_version}
License:        LPPL
Summary:        A pstricks-compatible graphicx for use with Plain TeX
Version:        svn21717.0.02

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pst-graphicx.tex) = %{tl_version}

%description -n texlive-pst-graphicx
The package provides a version of graphicx that avoids loading
the graphics bundle's (original) keyval package, which clashes
with pstricks' use of xkeyval.

%package -n texlive-pst-graphicx-doc
Summary:        Documentation for pst-graphicx
Version:        svn21717.0.02

Provides:       tex-pst-graphicx-doc
AutoReqProv:    No

%description -n texlive-pst-graphicx-doc
Documentation for pst-graphicx

%package -n texlive-pst-infixplot
Provides:       tex-pst-infixplot = %{tl_version}
License:        LPPL
Summary:        Using pstricks plotting capacities with infix expressions rather than RPN
Version:        svn15878.0.11

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(infix-RPN.tex) = %{tl_version}, tex(pst-infixplot.tex) = %{tl_version}
Provides:       tex(infix-RPN.sty) = %{tl_version}, tex(pst-infixplot.sty) = %{tl_version}

%description -n texlive-pst-infixplot
Plotting functions with pst-plot is very powerful but sometimes
difficult to learn since the syntax of \psplot and
\parametricplot requires some PostScript knowledge. The infix-
RPN and pst-infixplot styles simplify the usage of pst-plot for
the beginner, providing macro commands that convert natural
mathematical expressions to PostScript syntax.

%package -n texlive-pst-infixplot-doc
Summary:        Documentation for pst-infixplot
Version:        svn15878.0.11

Provides:       tex-pst-infixplot-doc
AutoReqProv:    No

%description -n texlive-pst-infixplot-doc
Documentation for pst-infixplot

%package -n texlive-pst-intersect
Provides:       tex-pst-intersect = %{tl_version}
License:        LPPL
Summary:        Compute intersections of arbitrary curves
Version:        svn33210.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(pst-xkey.sty), tex(pst-node.sty), tex(pst-func.sty)
Provides:       tex(pst-intersect.tex) = %{tl_version}, tex(pst-intersect.sty) = %{tl_version}

%description -n texlive-pst-intersect
The package computes the intersections between arbitrary
Postscript paths or Bezier curves, using the Bezier clipping
algorithm.

%package -n texlive-pst-intersect-doc
Summary:        Documentation for pst-intersect
Version:        svn33210.0.4

Provides:       tex-pst-intersect-doc
AutoReqProv:    No

%description -n texlive-pst-intersect-doc
Documentation for pst-intersect

%package -n texlive-pst-jtree
Provides:       tex-pst-jtree = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset complex trees for linguists
Version:        svn20946.2.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pst-jtree.tex) = %{tl_version}, tex(pst-jtree.sty) = %{tl_version}

%description -n texlive-pst-jtree
jTree uses PStricks to enable linguists to typeset complex
trees. The package requires use of PStricks (of course) and
xkeyval packages. jTree is a development of, and replacement
for, the jftree package, which is no longer available.

%package -n texlive-pst-jtree-doc
Summary:        Documentation for pst-jtree
Version:        svn20946.2.6

Provides:       tex-pst-jtree-doc
AutoReqProv:    No

%description -n texlive-pst-jtree-doc
Documentation for pst-jtree

%package -n texlive-pst-knot
Provides:       tex-pst-knot = %{tl_version}
License:        LPPL
Summary:        PSTricks package for displaying knots
Version:        svn16033.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-knot.tex) = %{tl_version}, tex(pst-knot.sty) = %{tl_version}

%description -n texlive-pst-knot
The package can produce a fair range of knot shapes, with all
the standard graphics controls one expects.

%package -n texlive-pst-knot-doc
Summary:        Documentation for pst-knot
Version:        svn16033.0.2

Provides:       tex-pst-knot-doc
AutoReqProv:    No

%description -n texlive-pst-knot-doc
Documentation for pst-knot

%package -n texlive-pst-labo
Provides:       tex-pst-labo = %{tl_version}
License:        LPPL
Summary:        Draw objects for Chemistry laboratories
Version:        svn39077

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-labo.tex) = %{tl_version}, tex(pst-laboObj.tex) = %{tl_version}
Provides:       tex(pst-labo.sty) = %{tl_version}

%description -n texlive-pst-labo
Pst-labo is a PSTricks related package for drawing basic and
complex chemical objects. The documentation of the package is
illuminated with plenty of illustrations together with their
source code, making it an easy read.

%package -n texlive-pst-labo-doc
Summary:        Documentation for pst-labo
Version:        svn39077

Provides:       tex-pst-labo-doc
AutoReqProv:    No

%description -n texlive-pst-labo-doc
Documentation for pst-labo

%package -n texlive-pst-layout
Provides:       tex-pst-layout = %{tl_version}
License:        LPPL
Summary:        Page layout macros based on PStricks packages
Version:        svn29803.95

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(ifthen.sty), tex(arrayjobx.sty)
Provides:       tex(pst-layout.sty) = %{tl_version}

%description -n texlive-pst-layout
The package provides a means of creating elaborate ("pseudo-
tabular") layouts of material, typically to be overlaid on an
included graphic. The package requires a recent version of the
package pst-node and some other pstricks-related material.

%package -n texlive-pst-layout-doc
Summary:        Documentation for pst-layout
Version:        svn29803.95

Provides:       tex-pst-layout-doc
AutoReqProv:    No

%description -n texlive-pst-layout-doc
Documentation for pst-layout

%package -n texlive-pst-lens
Provides:       tex-pst-lens = %{tl_version}
License:        LPPL
Summary:        Lenses with PSTricks
Version:        svn15878.1.02

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-lens.tex) = %{tl_version}, tex(pst-lens.sty) = %{tl_version}

%description -n texlive-pst-lens
This PSTricks package provides a really rather simple command
\PstLens that will draw a lens. Command parameters provide a
remarkable range of effects.

%package -n texlive-pst-lens-doc
Summary:        Documentation for pst-lens
Version:        svn15878.1.02

Provides:       tex-pst-lens-doc
AutoReqProv:    No

%description -n texlive-pst-lens-doc
Documentation for pst-lens

%package -n texlive-pst-light3d
Provides:       tex-pst-light3d = %{tl_version}
License:        LPPL
Summary:        Three dimensional lighting effects (PSTricks)
Version:        svn15878.0.12

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-light3d.tex) = %{tl_version}, tex(pst-light3d.sty) = %{tl_version}

%description -n texlive-pst-light3d
A PSTricks package for three dimensional lighting effects on
characters and PSTricks graphics, like lines, curves, plots,
...

%package -n texlive-pst-light3d-doc
Summary:        Documentation for pst-light3d
Version:        svn15878.0.12

Provides:       tex-pst-light3d-doc
AutoReqProv:    No

%description -n texlive-pst-light3d-doc
Documentation for pst-light3d

%package -n texlive-pst-magneticfield
Provides:       tex-pst-magneticfield = %{tl_version}
License:        LPPL
Summary:        Plotting a magnetic field with PSTricks
Version:        svn18922.1.13

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(pst-3d.sty), tex(multido.sty)
Provides:       tex(pst-magneticfield.tex) = %{tl_version}
Provides:       tex(pst-magneticfield.sty) = %{tl_version}

%description -n texlive-pst-magneticfield
pst-magneticfield is a PSTricks related package to draw the
magnetic field lines of Helmholtz coils in a two or three
dimensional view. There are several parameters to create a
different output. For more informations or some examples read
the documentation of the package.

%package -n texlive-pst-magneticfield-doc
Summary:        Documentation for pst-magneticfield
Version:        svn18922.1.13

Provides:       tex-pst-magneticfield-doc
AutoReqProv:    No

%description -n texlive-pst-magneticfield-doc
Documentation for pst-magneticfield

%package -n texlive-pst-math
Provides:       tex-pst-math = %{tl_version}
License:        LPPL
Summary:        Enhancement of PostScript math operators to use with pstricks
Version:        svn34786.0.63

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pst-math.tex) = %{tl_version}, tex(pst-math.sty) = %{tl_version}

%description -n texlive-pst-math
PostScript lacks a lot of basic operators such as tan, acos,
asin, cosh, sinh, tanh, acosh, asinh, atanh, exp (with e base).
Also (oddly) cos and sin use arguments in degrees. Pst-math
provides all those operators in a header file pst-math.pro with
wrappers pst-math.sty and pst-math.tex. In addition, sinc,
gauss, gammaln and bessel are implemented (only partially for
the latter). The package is designed essentially to work with
pst-plot but can be used in whatever PS code (such as pstricks
SpecialCoor "!", which is useful for placing labels). The
package also provides a routine SIMPSON for numerical
integration and a solver of linear equation systems.

%package -n texlive-pst-math-doc
Summary:        Documentation for pst-math
Version:        svn34786.0.63

Provides:       tex-pst-math-doc
AutoReqProv:    No

%description -n texlive-pst-math-doc
Documentation for pst-math

%package -n texlive-pst-mirror
Provides:       tex-pst-mirror = %{tl_version}
License:        LPPL
Summary:        Images on a spherical mirror
Version:        svn32997.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-mirror.tex) = %{tl_version}, tex(pst-mirror.sty) = %{tl_version}

%description -n texlive-pst-mirror
The package provides commands and supporting PostScript
material for drawing images as if reflected by a spherical
mirror.

%package -n texlive-pst-mirror-doc
Summary:        Documentation for pst-mirror
Version:        svn32997.1.01

Provides:       tex-pst-mirror-doc
AutoReqProv:    No

%description -n texlive-pst-mirror-doc
Documentation for pst-mirror

%package -n texlive-pst-node
Provides:       tex-pst-node = %{tl_version}
License:        LPPL
Summary:        Nodes and node connections in pstricks
Version:        svn46170
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-node.tex) = %{tl_version}, tex(pst-node97.tex) = %{tl_version}
Provides:       tex(pst-node.sty) = %{tl_version}, tex(pst-node97.sty) = %{tl_version}

%description -n texlive-pst-node
The package enables the user to connect information, and to
place labels, without knowing (in advance) the actual positions
of the items to be connected, or where the connecting line
should go. The macros are useful for making graphs and trees,
mathematical diagrams, linguistic syntax diagrams, and so on.
The package contents were previously distributed as a part of
the pstricks base distribution; the package serves as an
extension to PSTricks.

%package -n texlive-pst-node-doc
Summary:        Documentation for pst-node
Version:        svn46170
Provides:       tex-pst-node-doc
AutoReqProv:    No

%description -n texlive-pst-node-doc
Documentation for pst-node

%package -n texlive-pst-ob3d
Provides:       tex-pst-ob3d = %{tl_version}
License:        LPPL
Summary:        Three dimensional objects using PSTricks
Version:        svn15878.0.21

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-ob3d.tex) = %{tl_version}, tex(pst-ob3d.sty) = %{tl_version}

%description -n texlive-pst-ob3d
The package uses PSTricks to provide basic three-dimensional
objects. As yet, only cubes (which can be deformed to
rectangular parallelipipeds) and dies (which are only a special
kind of cubes) are defined.

%package -n texlive-pst-ob3d-doc
Summary:        Documentation for pst-ob3d
Version:        svn15878.0.21

Provides:       tex-pst-ob3d-doc
AutoReqProv:    No

%description -n texlive-pst-ob3d-doc
Documentation for pst-ob3d

%package -n texlive-pst-ode
Provides:       tex-pst-ode = %{tl_version}
License:        LPPL
Summary:        Solving initial value problems for sets of Ordinary Differential Equations
Version:        svn47959
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-ode.tex) = %{tl_version}, tex(pst-ode.sty) = %{tl_version}

%description -n texlive-pst-ode
The package defines \pstODEsolve for solving initial value
problems for sets of Ordinary Differential Equations (ODE)
using the Runge-Kutta-Fehlberg (RKF45) method with automatic
step size adjustment. The result is stored as a PostScript
object and may be plotted later using macros from other
PSTricks packages, such as \listplot (pst-plot) and
\listplotThreeD (pst-3dplot), or may be further processed by
user-defined PostScript procedures. Optionally, the computed
state vectors can be written as a table to a text file.

%package -n texlive-pst-ode-doc
Summary:        Documentation for pst-ode
Version:        svn47959
Provides:       tex-pst-ode-doc
AutoReqProv:    No

%description -n texlive-pst-ode-doc
Documentation for pst-ode

%package -n texlive-pst-optexp
Provides:       tex-pst-optexp = %{tl_version}
License:        LPPL 1.3
Summary:        Drawing optical experimental setups
Version:        svn35673.5.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(pstricks.sty), tex(pst-xkey.sty), tex(pst-node.sty)
Requires:       tex(pst-plot.sty), tex(multido.sty), tex(pst-eucl.sty), tex(pst-intersect.sty)
Requires:       tex(pstricks-add.sty), tex(environ.sty)
Provides:       tex(pst-optexp.sty) = %{tl_version}

%description -n texlive-pst-optexp
The package is a collection of optical components that
facilitate easy sketching of optical experimental setups. The
package uses PSTricks for its output. A wide range of free-ray
and fibre components is provided, the alignment, positioning
and labelling of which can be achieved in very simple and
flexible ways. The components may be connected with fibers or
beams, and realistic raytraced beam paths are also possible.

%package -n texlive-pst-optexp-doc
Summary:        Documentation for pst-optexp
Version:        svn35673.5.2

Provides:       tex-pst-optexp-doc
AutoReqProv:    No

%description -n texlive-pst-optexp-doc
Documentation for pst-optexp

%package -n texlive-pst-optic
Provides:       tex-pst-optic = %{tl_version}
License:        LPPL
Summary:        Drawing optics diagrams
Version:        svn41999
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-optic.tex) = %{tl_version}, tex(pst-optic.sty) = %{tl_version}

%description -n texlive-pst-optic
A package for drawing both reflective and refractive optics
diagrams. The package requires pstricks later than version
1.10.

%package -n texlive-pst-optic-doc
Summary:        Documentation for pst-optic
Version:        svn41999
Provides:       tex-pst-optic-doc
AutoReqProv:    No

%description -n texlive-pst-optic-doc
Documentation for pst-optic

%package -n texlive-pst-osci
Provides:       tex-pst-osci = %{tl_version}
License:        LPPL
Summary:        Oscgons with PSTricks
Version:        svn15878.2.82

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-osci.tex) = %{tl_version}, tex(pst-osci.sty) = %{tl_version}

%description -n texlive-pst-osci
pst-osci is a PSTricks package enables you to produce
oscilloscope "screen shots". Three channels can be used to
represent the most common signals (damped or not): namely
sinusoidal, rectangular, triangular, dog's tooth (left and
right oriented). The third channel allows you to add, to
subtract or to multiply the two other signals. Lissajous
diagrams (XY-mode) can also be obtained.

%package -n texlive-pst-osci-doc
Summary:        Documentation for pst-osci
Version:        svn15878.2.82

Provides:       tex-pst-osci-doc
AutoReqProv:    No

%description -n texlive-pst-osci-doc
Documentation for pst-osci

%package -n texlive-pst-ovl
Provides:       tex-pst-ovl = %{tl_version}
License:        LPPL
Summary:        Create and manage graphical overlays
Version:        svn45506
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(pst-ovl.tex) = %{tl_version}, tex(pst-ovl.sty) = %{tl_version}

%description -n texlive-pst-ovl
The package is useful when building an image from assorted
material, as in the slides of a projected presentation. The
package requires pstricks, and shares that package's
restrictions on usage when generating PDF output.

%package -n texlive-pst-ovl-doc
Summary:        Documentation for pst-ovl
Version:        svn45506
Provides:       tex-pst-ovl-doc
AutoReqProv:    No

%description -n texlive-pst-ovl-doc
Documentation for pst-ovl

%package -n texlive-pst-pad
Provides:       tex-pst-pad = %{tl_version}
License:        LPPL
Summary:        Draw simple attachment systems with PSTricks
Version:        svn15878.0.3b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-pad.tex) = %{tl_version}, tex(pst-pad.sty) = %{tl_version}

%description -n texlive-pst-pad
The package collects a set of graphical elements based on
PStricks that can be used to facilitate display of attachment
systems such as two differently shaped surfaces with or without
a fluid wedged in between. These macros ease the display of wet
adhesion models and common friction systems such as boundary
lubrication, elastohydrodynamic lubrication and hydrodynamic
lubrication.

%package -n texlive-pst-pad-doc
Summary:        Documentation for pst-pad
Version:        svn15878.0.3b

Provides:       tex-pst-pad-doc
AutoReqProv:    No

%description -n texlive-pst-pad-doc
Documentation for pst-pad

%package -n texlive-pst-pdgr
Provides:       tex-pst-pdgr = %{tl_version}
License:        LPPL
Summary:        Draw medical pedigrees using pstricks
Version:        svn45875
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(pst-pdgr.tex) = %{tl_version}, tex(pst-pdgr.cfg) = %{tl_version}
Provides:       tex(pst-pdgr.sty) = %{tl_version}

%description -n texlive-pst-pdgr
The package provides a set of macros based on PSTricks to draw
medical pedigrees according to the recommendations for
standardized human pedigree nomenclature. The drawing commands
place the symbols on a pspicture canvas. An interface for
making trees is also provided. The package may be used both
with LaTeX and PlainTeX. A separate Perl program for generating
TeX files from spreadsheets is available.

%package -n texlive-pst-pdgr-doc
Summary:        Documentation for pst-pdgr
Version:        svn45875
Provides:       tex-pst-pdgr-doc
AutoReqProv:    No

%description -n texlive-pst-pdgr-doc
Documentation for pst-pdgr

%package -n texlive-pst-perspective
Provides:       tex-pst-perspective = %{tl_version}
License:        LPPL 1.3
Summary:        Draw perspective views using pstricks
Version:        svn39585

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(pst-grad.sty)
Provides:       tex(pst-perspective.tex) = %{tl_version}
Provides:       tex(pst-perspective.sty) = %{tl_version}

%description -n texlive-pst-perspective
The package provides the means to draw an orthogonal parallel
projection with an arbitrarily chosen angle and a variable
shortening factor.

%package -n texlive-pst-perspective-doc
Summary:        Documentation for pst-perspective
Version:        svn39585

Provides:       tex-pst-perspective-doc
AutoReqProv:    No

%description -n texlive-pst-perspective-doc
Documentation for pst-perspective

%package -n texlive-pst-platon
Provides:       tex-pst-platon = %{tl_version}
License:        LPPL
Summary:        Platonic solids in PSTricks
Version:        svn16538.0.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(pst-3d.sty), tex(pst-xkey.sty)
Provides:       tex(pst-platon.sty) = %{tl_version}

%description -n texlive-pst-platon
The package adds to PSTricks the ability to draw 3-dimensional
views of the five Platonic solids.

%package -n texlive-pst-platon-doc
Summary:        Documentation for pst-platon
Version:        svn16538.0.01

Provides:       tex-pst-platon-doc
AutoReqProv:    No

%description -n texlive-pst-platon-doc
Documentation for pst-platon

%package -n texlive-pst-plot
Provides:       tex-pst-plot = %{tl_version}
License:        LPPL
Summary:        Plot data using PSTricks
Version:        svn47163
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty), tex(pst-xkey.sty), tex(multido.sty)
Provides:       tex(pst-plot.tex) = %{tl_version}, tex(pst-plot97.tex) = %{tl_version}
Provides:       tex(pst-plot.sty) = %{tl_version}

%description -n texlive-pst-plot
The package provides plotting of data (typically from external
files), using PSTricks. Plots may be configured using a wide
variety of parameters.

%package -n texlive-pst-plot-doc
Summary:        Documentation for pst-plot
Version:        svn47163
Provides:       tex-pst-plot-doc
AutoReqProv:    No

%description -n texlive-pst-plot-doc
Documentation for pst-plot

%package -n texlive-pst-poly
Provides:       tex-pst-poly = %{tl_version}
License:        LPPL
Summary:        Polygons with PSTricks
Version:        svn35062.1.63

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-poly.tex) = %{tl_version}, tex(pst-poly.sty) = %{tl_version}

%description -n texlive-pst-poly
This PSTricks package provides a really rather simple command
\PstPolygon that will draw various regular and non-regular
polygons (according to command parameters); various shortcuts
to commonly-used polygons are provided, as well as a command
\pspolygonbox that frames text with a polygon. The package uses
the xkeyval package for argument decoding.

%package -n texlive-pst-poly-doc
Summary:        Documentation for pst-poly
Version:        svn35062.1.63

Provides:       tex-pst-poly-doc
AutoReqProv:    No

%description -n texlive-pst-poly-doc
Documentation for pst-poly

%package -n texlive-pst-pulley
Provides:       tex-pst-pulley = %{tl_version}
License:        LPPL 1.3
Summary:        Plot pulleys, using pstricks
Version:        svn45316
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-pulley.tex) = %{tl_version}, tex(pst-pulley.sty) = %{tl_version}

%description -n texlive-pst-pulley
The package enables the user to draw pulley systems with up to
6 pulleys. The pulley diagrams are labelled with the physical
properties of the system. The package uses pstricks, and
requires a several pstricks-related packages.

%package -n texlive-pst-pulley-doc
Summary:        Documentation for pst-pulley
Version:        svn45316
Provides:       tex-pst-pulley-doc
AutoReqProv:    No

%description -n texlive-pst-pulley-doc
Documentation for pst-pulley

%package -n texlive-pst-qtree
Provides:       tex-pst-qtree = %{tl_version}
License:        GPL+
Summary:        Simple syntax for trees
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pst-qtree.tex) = %{tl_version}, tex(pst-qtree.sty) = %{tl_version}

%description -n texlive-pst-qtree
The package provides a qtree-like front end for PSTricks.

%package -n texlive-pst-qtree-doc
Summary:        Documentation for pst-qtree
Version:        svn15878.0

Provides:       tex-pst-qtree-doc
AutoReqProv:    No

%description -n texlive-pst-qtree-doc
Documentation for pst-qtree

%package -n texlive-pst-rubans
Provides:       tex-pst-rubans = %{tl_version}
License:        LPPL
Summary:        Draw three-dimensional ribbons
Version:        svn23464.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-rubans.tex) = %{tl_version}, tex(pst-rubans.sty) = %{tl_version}

%description -n texlive-pst-rubans
The package uses PStricks and pst-solides3d to draw three
dimensional ribbons on a cylinder, torus, sphere, cone or
paraboloid. The width of the ribbon, the number of turns, the
colour of the outer and the inner surface of the ribbon may be
set. In the case of circular and conical helices, one may also
choose the number of ribbons.

%package -n texlive-pst-rubans-doc
Summary:        Documentation for pst-rubans
Version:        svn23464.1.2

Provides:       tex-pst-rubans-doc
AutoReqProv:    No

%description -n texlive-pst-rubans-doc
Documentation for pst-rubans

%package -n texlive-pst-sigsys
Provides:       tex-pst-sigsys = %{tl_version}
License:        LPPL
Summary:        Support of signal processing-related disciplines
Version:        svn21667.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-sigsys.tex) = %{tl_version}, tex(pst-sigsys.sty) = %{tl_version}

%description -n texlive-pst-sigsys
The package offers a collection of useful macros for
disciplines related to signal processing. It defines macros for
plotting a sequence of numbers, drawing the pole-zero diagram
of a system, shading the region of convergence, creating an
adder or a multiplier node, placing a framed node at a given
coordinate, creating an up-sampler or a down-sampler node,
drawing the block diagram of a system, drawing adaptive
systems, sequentially connecting a list of nodes, and
connecting a list of nodes using any node-connecting macro.

%package -n texlive-pst-sigsys-doc
Summary:        Documentation for pst-sigsys
Version:        svn21667.1.4

Provides:       tex-pst-sigsys-doc
AutoReqProv:    No

%description -n texlive-pst-sigsys-doc
Documentation for pst-sigsys

%package -n texlive-pst-slpe
Provides:       tex-pst-slpe = %{tl_version}
License:        LPPL
Summary:        Sophisticated colour gradients
Version:        svn24391.1.31

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-slpe.tex) = %{tl_version}, tex(pst-slpe.sty) = %{tl_version}

%description -n texlive-pst-slpe
This PStricks package covers all the colour gradient
functionality of pst-grad (part of the base pstricks
distribution), and provides the following facilities: it
permits the user to specify an arbitrary number of colours,
along with the points at which they are to be reached; it
converts between RGB and HSV behind the scenes; it provides
concentric and radial gradients; it provides a command \psBall
that generates bullets with a three-dimensional appearance; and
uses the xkeyval package for the extended key handling.

%package -n texlive-pst-slpe-doc
Summary:        Documentation for pst-slpe
Version:        svn24391.1.31

Provides:       tex-pst-slpe-doc
AutoReqProv:    No

%description -n texlive-pst-slpe-doc
Documentation for pst-slpe

%package -n texlive-pst-solarsystem
Provides:       tex-pst-solarsystem = %{tl_version}
License:        LPPL
Summary:        Plot the solar system for a specific date
Version:        svn45097
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-solarsystem.tex) = %{tl_version}
Provides:       tex(pst-solarsystem.sty) = %{tl_version}

%description -n texlive-pst-solarsystem
The package uses pstricks to produce diagrams of the visible
planets, projected on the plane of the ecliptic. It is not
possible to represent all the planets in their real
proportions, so only Mercury, Venus, Earth and Mars have their
orbits in correct proportions and their relative sizes are
observed. Saturn and Jupiter are in the right direction, but
not in the correct size.

%package -n texlive-pst-solarsystem-doc
Summary:        Documentation for pst-solarsystem
Version:        svn45097
Provides:       tex-pst-solarsystem-doc
AutoReqProv:    No

%description -n texlive-pst-solarsystem-doc
Documentation for pst-solarsystem

%package -n texlive-pst-solides3d
Provides:       tex-pst-solides3d = %{tl_version}
License:        LPPL 1.3
Summary:        Draw perspective views of 3D solids
Version:        svn45113
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-solides3d.tex) = %{tl_version}, tex(pst-solides3d.sty) = %{tl_version}

%description -n texlive-pst-solides3d
The package is designed to draw solids in 3d perspective.
Features include: create primitive solids; create solids by
including a list of its vertices and faces; faces of solids and
surfaces can be colored by choosing from a very large palette
of colors; draw parametric surfaces in algebraic and reverse
polish notation; create explicit and parameterized algebraic
functions drawn in 2 or 3 dimensions; project text onto a plane
or onto the faces of a solid; support for including external
database files.

%package -n texlive-pst-solides3d-doc
Summary:        Documentation for pst-solides3d
Version:        svn45113
Provides:       tex-pst-solides3d-doc
AutoReqProv:    No

%description -n texlive-pst-solides3d-doc
Documentation for pst-solides3d

%package -n texlive-pst-soroban
Provides:       tex-pst-soroban = %{tl_version}
License:        LPPL
Summary:        Draw a Soroban using PSTricks
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks-add.sty), tex(calc.sty), tex(ifthen.sty)
Provides:       tex(pst-soroban.sty) = %{tl_version}

%description -n texlive-pst-soroban
The package uses PSTricks to draw a Japanese abacus, or
soroban. The soroban is still used in Japan today.

%package -n texlive-pst-soroban-doc
Summary:        Documentation for pst-soroban
Version:        svn15878.1.0

Provides:       tex-pst-soroban-doc
AutoReqProv:    No

%description -n texlive-pst-soroban-doc
Documentation for pst-soroban

%package -n texlive-pst-spectra
Provides:       tex-pst-spectra = %{tl_version}
License:        LPPL
Summary:        Draw continuum, emission and absorption spectra with PSTricks
Version:        svn15878.0.91

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(multido.sty), tex(xkeyval.sty)
Provides:       tex(pst-spectra.tex) = %{tl_version}, tex(pst-spectra.sty) = %{tl_version}

%description -n texlive-pst-spectra
The package is a PSTricks extension, based on a NASA lines
database. It allows you to draw continuum, emission and
absorption spectra. A Total of 16 880 visible lines from 99
elements can be displayed. The package requires the xkeyval
package for decoding its arguments.

%package -n texlive-pst-spectra-doc
Summary:        Documentation for pst-spectra
Version:        svn15878.0.91

Provides:       tex-pst-spectra-doc
AutoReqProv:    No

%description -n texlive-pst-spectra-doc
Documentation for pst-spectra

%package -n texlive-pst-spirograph
Provides:       tex-pst-spirograph = %{tl_version}
License:        LPPL
Summary:        Drawing hypotrochoids as with a spirograph
Version:        svn35026.0.41

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-spirograph.tex) = %{tl_version}, tex(pst-spirograph.sty) = %{tl_version}

%description -n texlive-pst-spirograph
The package simulates the action of a spirograph, which is a
geometric drawing toy that produces mathematical roulette
curves (technically known as hypotrochoids and epitrochoids).

%package -n texlive-pst-spirograph-doc
Summary:        Documentation for pst-spirograph
Version:        svn35026.0.41

Provides:       tex-pst-spirograph-doc
AutoReqProv:    No

%description -n texlive-pst-spirograph-doc
Documentation for pst-spirograph

%package -n texlive-pst-stru
Provides:       tex-pst-stru = %{tl_version}
License:        LPPL
Summary:        Civil engineering diagrams, using pstricks
Version:        svn38613

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(multido.sty)
Provides:       tex(pst-stru.tex) = %{tl_version}, tex(pst-stru.sty) = %{tl_version}

%description -n texlive-pst-stru
The package is a PSTricks-based, and provides facilities to
draw structural schemes in civil engineering analysis, for
beams, portals, arches and piles.

%package -n texlive-pst-stru-doc
Summary:        Documentation for pst-stru
Version:        svn38613

Provides:       tex-pst-stru-doc
AutoReqProv:    No

%description -n texlive-pst-stru-doc
Documentation for pst-stru

%package -n texlive-pst-support-doc
Summary:        Documentation for pst-support
Version:        svn15878.0

Provides:       tex-pst-support-doc
AutoReqProv:    No

%description -n texlive-pst-support-doc
Documentation for pst-support

%package -n texlive-pst-text
Provides:       tex-pst-text = %{tl_version}
License:        LPPL
Summary:        Text and character manipulation in PSTricks
Version:        svn15878.1.00

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-char.tex) = %{tl_version}, tex(pst-text.tex) = %{tl_version}
Provides:       tex(pst-char.sty) = %{tl_version}, tex(pst-text.sty) = %{tl_version}

%description -n texlive-pst-text
Pst-text is a PSTricks based package for plotting text along a
different path and manipulating characters. It includes the
functionality of the old package pst-char.

%package -n texlive-pst-text-doc
Summary:        Documentation for pst-text
Version:        svn15878.1.00

Provides:       tex-pst-text-doc
AutoReqProv:    No

%description -n texlive-pst-text-doc
Documentation for pst-text

%package -n texlive-pst-thick
Provides:       tex-pst-thick = %{tl_version}
License:        LPPL
Summary:        Drawing very thick lines and curves
Version:        svn16369.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-thick.tex) = %{tl_version}, tex(pst-thick.sty) = %{tl_version}

%description -n texlive-pst-thick
The package supports drawing of very thick lines and curves in
PSTricks, with various fillings for the body of the lines.

%package -n texlive-pst-thick-doc
Summary:        Documentation for pst-thick
Version:        svn16369.1.0

Provides:       tex-pst-thick-doc
AutoReqProv:    No

%description -n texlive-pst-thick-doc
Documentation for pst-thick

%package -n texlive-pst-tools
Provides:       tex-pst-tools = %{tl_version}
License:        LPPL
Summary:        PStricks support functions
Version:        svn45978
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-tools.tex) = %{tl_version}, tex(pst-tools.sty) = %{tl_version}

%description -n texlive-pst-tools
The package provides helper functions for other PSTricks
related packages.

%package -n texlive-pst-tools-doc
Summary:        Documentation for pst-tools
Version:        svn45978
Provides:       tex-pst-tools-doc
AutoReqProv:    No

%description -n texlive-pst-tools-doc
Documentation for pst-tools

%package -n texlive-pst-tree
Provides:       tex-pst-tree = %{tl_version}
License:        LPPL
Summary:        Trees, using pstricks
Version:        svn43272
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty)
Provides:       tex(pst-tree.tex) = %{tl_version}, tex(pst-tree.sty) = %{tl_version}

%description -n texlive-pst-tree
pst-tree is a pstricks package that defines a macro \pstree
which offers a structured way of joining nodes created using
pst-node in order to draw trees.

%package -n texlive-pst-tree-doc
Summary:        Documentation for pst-tree
Version:        svn43272
Provides:       tex-pst-tree-doc
AutoReqProv:    No

%description -n texlive-pst-tree-doc
Documentation for pst-tree

%package -n texlive-pst-tvz
Provides:       tex-pst-tvz = %{tl_version}
License:        LPPL 1.3
Summary:        Draw trees with more than one root node, using PSTricks
Version:        svn23451.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-tvz.tex) = %{tl_version}, tex(pst-tvz.sty) = %{tl_version}

%description -n texlive-pst-tvz
The package uses PSTricks to draw trees with more than one root
node. It is similar to pst-tree, though it uses a different
placement algorithm.

%package -n texlive-pst-tvz-doc
Summary:        Documentation for pst-tvz
Version:        svn23451.1.01

Provides:       tex-pst-tvz-doc
AutoReqProv:    No

%description -n texlive-pst-tvz-doc
Documentation for pst-tvz

%package -n texlive-pst-uml
Provides:       tex-pst-uml = %{tl_version}
License:        LPPL
Summary:        UML diagrams with PSTricks
Version:        svn15878.0.83

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex-multido, tex(pstricks.sty), tex(pst-node.sty), tex(pst-tree.sty)
Requires:       tex(multido.sty), tex(calc.sty), tex(ifthen.sty), tex(graphicx.sty)
Requires:       tex(pst-xkey.sty)
Provides:       tex(pst-uml.sty) = %{tl_version}

%description -n texlive-pst-uml
pst-uml is a PSTricks package that provides support for drawing
moderately complex UML (Universal Modelling Language) diagrams.
(The PDF documentation is written in French.)

%package -n texlive-pst-uml-doc
Summary:        Documentation for pst-uml
Version:        svn15878.0.83

Provides:       tex-pst-uml-doc
AutoReqProv:    No
Requires:       tex-multido-doc

%description -n texlive-pst-uml-doc
Documentation for pst-uml

%package -n texlive-pst-vectorian
Provides:       tex-pst-vectorian = %{tl_version}
License:        LPPL
Summary:        Printing ornaments
Version:        svn28801.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(pstricks.sty)
Provides:       tex(psvectorian.sty) = %{tl_version}

%description -n texlive-pst-vectorian
The package uses PStricks to draw ornaments (a substantial
repertoire of ornaments is provided).

%package -n texlive-pst-vectorian-doc
Summary:        Documentation for pst-vectorian
Version:        svn28801.0.4

Provides:       tex-pst-vectorian-doc
AutoReqProv:    No

%description -n texlive-pst-vectorian-doc
Documentation for pst-vectorian

%package -n texlive-pst-vowel
Provides:       tex-pst-vowel = %{tl_version}
License:        LPPL
Summary:        Enable arrows showing diphthongs on vowel charts
Version:        svn25228.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pst-node.sty), tex(vowel.sty)
Provides:       tex(pst-vowel.sty) = %{tl_version}

%description -n texlive-pst-vowel
The package extends the vowel package (distributed as part of
the tipa bundle) by allowing the user to draw arrows between
vowels to show relationships such as diphthong membership. The
package depends on use of pstricks.

%package -n texlive-pst-vowel-doc
Summary:        Documentation for pst-vowel
Version:        svn25228.1.0

Provides:       tex-pst-vowel-doc
AutoReqProv:    No

%description -n texlive-pst-vowel-doc
Documentation for pst-vowel

%package -n texlive-pst-vue3d
Provides:       tex-pst-vue3d = %{tl_version}
License:        LPPL
Summary:        Draw perspective views of three dimensional objects
Version:        svn15878.1.24

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty)
Provides:       tex(pst-vue3d.tex) = %{tl_version}, tex(pst-vue3d.sty) = %{tl_version}

%description -n texlive-pst-vue3d
With pst-vue3d three dimensional objects like cubes, spheres
and others can be viewed from different points. The
distribution includes a comprehensive set of examples of usage.

%package -n texlive-pst-vue3d-doc
Summary:        Documentation for pst-vue3d
Version:        svn15878.1.24

Provides:       tex-pst-vue3d-doc
AutoReqProv:    No

%description -n texlive-pst-vue3d-doc
Documentation for pst-vue3d

%package -n texlive-pstricks
Provides:       tex-pstricks = %{tl_version}
License:        LPPL 1.3
Summary:        PostScript macros for TeX
Version:        svn48256
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-pst-tools, tex(pst-plot.sty), tex(pst-node.sty), tex(pst-tree.sty)
Requires:       tex(pst-grad.sty), tex(pst-coil.sty), tex(pst-text.sty), tex(pst-3d.sty)
Requires:       tex(pst-eps.sty), tex(pst-fill.sty), tex(pstricks-add.sty), tex(multido.sty)
Requires:       tex(xcolor.sty), tex(fontenc.sty), tex(ifpdf.sty), tex(textcomp.sty)
Requires:       tex(bera.sty), tex(xspace.sty), tex(makeidx.sty), tex(calc.sty)
Requires:       tex(babel.sty), tex(xkeyval.sty), tex(pst-xkey.sty), tex(xkvview.sty)
Requires:       tex(lscape.sty), tex(graphicx.sty), tex(eso-pic.sty), tex(amsmath.sty)
Requires:       tex(amssymb.sty), tex(tabularx.sty), tex(ragged2e.sty), tex(booktabs.sty)
Requires:       tex(footmisc.sty), tex(chngcntr.sty), tex(nameref.sty), tex(varioref.sty)
Requires:       tex(subfig.sty), tex(setspace.sty), tex(paralist.sty), tex(fancyvrb.sty)
Requires:       tex(filecontents.sty), tex(showexpl.sty)
Requires:       tex(scrpage2.sty), tex(caption.sty), tex(hyperref.sty), tex(breakurl.sty)
Requires:       tex(auto-pst-pdf.sty), tex(pst-ovl.sty)
Provides:       tex(README.cfg) = %{tl_version}, tex(distiller.cfg) = %{tl_version}
Provides:       tex(dvips.cfg) = %{tl_version}, tex(dvipsone.cfg) = %{tl_version}
Provides:       tex(gastex.cfg) = %{tl_version}, tex(textures.cfg) = %{tl_version}
Provides:       tex(vtex.cfg) = %{tl_version}, tex(xdvipdfmx.cfg) = %{tl_version}
Provides:       tex(pst-fp.tex) = %{tl_version}, tex(pst-key.tex) = %{tl_version}
Provides:       tex(pstricks.tex) = %{tl_version}, tex(pstricks97.tex) = %{tl_version}
Provides:       tex(pst-all.sty) = %{tl_version}, tex(pst-doc.cls) = %{tl_version}
Provides:       tex(pst-key.sty) = %{tl_version}, tex(pstcol.sty) = %{tl_version}
Provides:       tex(pstricks.sty) = %{tl_version}

%description -n texlive-pstricks
PSTricks offers an extensive collection of macros for
generating PostScript that is usable with most TeX macro
formats, including Plain TeX, LaTeX, AMS-TeX, and AMS-LaTeX.
Included are macros for colour, graphics, pie charts, rotation,
trees and overlays. It has many special features, including a
wide variety of graphics (picture drawing) macros, with a
flexible interface and with colour support. There are macros
for colouring or shading the cells of tables. The package
pstricks-add contains bug-fixes and additions for PSTricks
(among other things). PSTricks ordinarily uses PostScript
\special commands, which are not supported by pdf(La)TeX. This
limitation may be overcome by using either the pst-pdf or the
pdftricks package, to generate a PDF inclusion from a PSTricks
diagram. PSTricks macros can also generate PDF output when the
document is processed XeTeX, without the need for other
supporting packages. Note that this is one of a pair of
catalogue entries for PSTricks; the other one (PSTricks) is
acting as a "stub", while editorial work on catalogue entries
for PSTricks contributed is completed.

%package -n texlive-pstricks-doc
Summary:        Documentation for pstricks
Version:        svn48256
Provides:       tex-pstricks-doc
AutoReqProv:    No

%description -n texlive-pstricks-doc
Documentation for pstricks

%package -n texlive-pstricks-add
Provides:       tex-pstricks-add = %{tl_version}
License:        LPPL
Summary:        A collection of add-ons and bugfixes for PSTricks
Version:        svn46541
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pstricks.sty), tex(pst-plot.sty), tex(pst-node.sty), tex(pst-3d.sty)
Requires:       tex(pst-math.sty), tex(multido.sty)
Provides:       tex(pstricks-add.tex) = %{tl_version}, tex(pstricks-add.cfg) = %{tl_version}
Provides:       tex(pstricks-add.sty) = %{tl_version}

%description -n texlive-pstricks-add
Collects together examples that have been posted to the
pstricks mailing list, together with many additional features
for the basic pstricks, pst-plot and pst-node, including:
bugfixes; new options for the pspicture environment; arrows;
braces as node connection/linestyle; extended axes for plots
(e.g., logarithm axes); polar plots; plotting tangent lines of
curves or functions; solving and printing differential
equations; box plots; matrix plots; and pie charts. The package
makes use of PostScript routines provided by pst-math.

%package -n texlive-pstricks-add-doc
Summary:        Documentation for pstricks-add
Version:        svn46541
Provides:       tex-pstricks-add-doc
AutoReqProv:    No

%description -n texlive-pstricks-add-doc
Documentation for pstricks-add

%package -n texlive-pstricks_calcnotes-doc
Summary:        Documentation for pstricks_calcnotes
Version:        svn34363.1.2

Provides:       tex-pstricks_calcnotes-doc
AutoReqProv:    No

%description -n texlive-pstricks_calcnotes-doc
Documentation for pstricks_calcnotes

%package -n texlive-pracjourn
Provides:       tex-pracjourn = %{tl_version}
License:        GPL+
Summary:        Typeset articles for PracTeX
Version:        svn15878.0.4n

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(lmodern.sty), tex(mathpazo.sty), tex(microtype.sty), tex(textcomp.sty)
Requires:       tex(color.sty), tex(hyperref.sty), tex(graphicx.sty)
Provides:       tex(pracjourn.cls) = %{tl_version}

%description -n texlive-pracjourn
The pracjourn class is used for typesetting articles in the
PracTeX Journal. It is based on the article class with
modifications to allow for more flexible front-matter and
revision control, among other small changes.

%package -n texlive-pracjourn-doc
Summary:        Documentation for pracjourn
Version:        svn15878.0.4n

Provides:       tex-pracjourn-doc
AutoReqProv:    No

%description -n texlive-pracjourn-doc
Documentation for pracjourn

%package -n texlive-procIAGssymp
Provides:       tex-procIAGssymp = %{tl_version}
License:        LPPL
Summary:        Macros for IAG symposium papers
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(procIAGssymp.sty) = %{tl_version}

%description -n texlive-procIAGssymp
This package provides (re-)definitions of some LaTeX commands
that can be useful for the preparation of a paper with the
style of the proceeding of symposia sponsored by the
'International Association of Geodesy (IAG)' published by
Springer-Verlag.

%package -n texlive-procIAGssymp-doc
Summary:        Documentation for procIAGssymp
Version:        svn15878.0

Provides:       tex-procIAGssymp-doc
AutoReqProv:    No

%description -n texlive-procIAGssymp-doc
Documentation for procIAGssymp

%package -n texlive-proposal
Provides:       tex-proposal = %{tl_version}
License:        LPPL
Summary:        A class for preparing proposals
Version:        svn40538

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(workaddress.sty), tex(eurosym.sty), tex(xspace.sty), tex(amssymb.sty)
Requires:       tex(url.sty), tex(graphicx.sty), tex(colortbl.sty), tex(xcolor.sty)
Requires:       tex(rotating.sty), tex(fancyhdr.sty), tex(array.sty), tex(comment.sty)
Requires:       tex(tikz.sty), tex(paralist.sty), tex(a4wide.sty), tex(boxedminipage.sty)
Requires:       tex(helvet.sty), tex(textcomp.sty), tex(biblatex.sty), tex(csquotes.sty)
Requires:       tex(mdframed.sty), tex(hyperref.sty), tex(ed.sty), tex(svninfo.sty)
Requires:       tex(babel.sty), tex(longtable.sty), tex(wrapfig.sty)
Provides:       tex(pdata.sty) = %{tl_version}, tex(proposal.cls) = %{tl_version}
Provides:       tex(reporting.cls) = %{tl_version}, tex(reporting.sty) = %{tl_version}
Provides:       tex(dfgpdata.sty) = %{tl_version}, tex(dfgproposal.cls) = %{tl_version}
Provides:       tex(dfgreporting.cls) = %{tl_version}, tex(dfgreporting.sty) = %{tl_version}
Provides:       tex(eupdata.sty) = %{tl_version}, tex(eudata.sty) = %{tl_version}
Provides:       tex(euproposal.cls) = %{tl_version}, tex(eureporting.cls) = %{tl_version}
Provides:       tex(eureporting.sty) = %{tl_version}

%description -n texlive-proposal
The process of preparing a collaborative proposal, to a major
funding body, involves integration of contributions of a many
people at many sites. It is therefore an ideal application for
a text-based document preparation system such as LaTeX, in
concert with a distributed version control system such as SVN.
The proposal class itself provides a basis for such an
enterprise. The dfgproposal and dfgproposal classes provide two
specialisations of the base class for (respectively) German and
European research proposals. The packages depend on the
author's stex bundle.

%package -n texlive-proposal-doc
Summary:        Documentation for proposal
Version:        svn40538

Provides:       tex-proposal-doc
AutoReqProv:    No

%description -n texlive-proposal-doc
Documentation for proposal

%package -n texlive-ptptex
Provides:       tex-ptptex = %{tl_version}
License:        LPPL
Summary:        Macros for 'Progress of Theoretical Physics'
Version:        svn19440.0.91

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty), tex(amssymb.sty), tex(overcite.sty), tex(wrapfig.sty)
Provides:       tex(ptp-prep.clo) = %{tl_version}, tex(ptptex.cls) = %{tl_version}
Provides:       tex(wrapft.sty) = %{tl_version}

%description -n texlive-ptptex
The distribution contains the class (which offers an option
file for preprints), and a template. The class requires the
cite, overcite and wrapfig packages.

%package -n texlive-ptptex-doc
Summary:        Documentation for ptptex
Version:        svn19440.0.91

Provides:       tex-ptptex-doc
AutoReqProv:    No

%description -n texlive-ptptex-doc
Documentation for ptptex

%package -n texlive-psu-thesis
Provides:       tex-psu-thesis = %{tl_version}
License:        LPPL
Summary:        Package for writing a thesis at Penn State University
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(setspace.sty)
Provides:       tex(psu-thesis.sty) = %{tl_version}

%description -n texlive-psu-thesis
The package provides proper page formatting according to the
Penn State thesis office guidelines (as of 2004) and
automatically formats the front and back matter, title page,
and more. A BibTeX style file is also included for the
bibliography.

%package -n texlive-psu-thesis-doc
Summary:        Documentation for psu-thesis
Version:        svn15878.1.1

Provides:       tex-psu-thesis-doc
AutoReqProv:    No

%description -n texlive-psu-thesis-doc
Documentation for psu-thesis

%package -n texlive-pseudocode
Provides:       tex-pseudocode = %{tl_version}
License:        LPPL
Summary:        LaTeX environment for specifying algorithms in a natural way
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fancybox.sty), tex(ifthen.sty)
Provides:       tex(pseudocode.sty) = %{tl_version}

%description -n texlive-pseudocode
This package provides the environment "pseudocode" for
describing algorithms in a natural manner.

%package -n texlive-pseudocode-doc
Summary:        Documentation for pseudocode
Version:        svn15878.0

Provides:       tex-pseudocode-doc
AutoReqProv:    No

%description -n texlive-pseudocode-doc
Documentation for pseudocode

%package -n texlive-ptext
Provides:       tex-ptext = %{tl_version}
License:        LPPL 1.2
Summary:        A 'lipsum' for Persian
Version:        svn30171.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(biditools.sty)
Provides:       tex(ptext.sty) = %{tl_version}

%description -n texlive-ptext
The package provides lipsum-like facilities for the Persian
language. The source of the filling text is the Persian epic
"the Shanameh" (100 paragraphs are used.) The package needs to
be run under XeLaTeX.

%package -n texlive-ptext-doc
Summary:        Documentation for ptext
Version:        svn30171.1.1

Provides:       tex-ptext-doc
AutoReqProv:    No

%description -n texlive-ptext-doc
Documentation for ptext

%package -n texlive-prooftrees-doc
Provides:       tex-prooftrees-doc = %{tl_version}
License:        LPPL
Summary:        doc files of prooftrees
Version:        svn43184
AutoReqProv:    No

%description -n texlive-prooftrees-doc
Documentation for prooftrees

%package -n texlive-prooftrees
Provides:       tex-prooftrees = %{tl_version}
License:        LPPL
Summary:        Forest-based proof trees (symbolic logic)
Version:        svn43184
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(prooftrees.sty) = %{tl_version}

%description -n texlive-prooftrees
The package supports drawing proof trees of the kind often used
in introductory logic classes, especially those aimed at
students without strong mathemtical backgrounds. Hodges (1991)
is one example of a text which uses this system. When teaching
such a system it is especially useful to annotate the tree with
line numbers, justifications and explanations of branch
closures. prooftrees provides a single environment, prooftree,
and a variety of tools for annotating, customising and
highlighting such trees. A cross-referencing system is provided
for trees which cite line numbers in justifications for proof
lines or branch closures. prooftrees is based on forest and,
hence, TikZ. The package requires version 2.0.2 of Forest for
expected results and will not work with version 1.

%package -n texlive-pst-cie-doc
Provides:       tex-pst-cie-doc = %{tl_version}
License:        LPPL
Summary:        doc files of pst-cie
Version:        svn45111
AutoReqProv:    No

%description -n texlive-pst-cie-doc
Documentation for pst-cie

%package -n texlive-pst-cie
Provides:       tex-pst-cie = %{tl_version}
License:        LPPL
Summary:        CIE color space
Version:        svn45111
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(pst-cie.sty) = %{tl_version}, tex(pst-cie.tex) = %{tl_version}

%description -n texlive-pst-cie
pst-cie is a PSTricks related package to show the different CIE
color spaces: Adobe, CIE, ColorMatch, NTSC, Pal-Secam,
ProPhoto, SMPTE, and sRGB.

%package -n texlive-ptex-fonts
Provides:       tex-ptex-fonts = %{tl_version}
License:        BSD
Summary:        Fonts for use with pTeX
Version:        svn46940
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(ascgrp.mf) = %{tl_version}, tex(ascii.mf) = %{tl_version}
Provides:       tex(ascii10.mf) = %{tl_version}, tex(ascii36.mf) = %{tl_version}
Provides:       tex(jis-v.pl) = %{tl_version}, tex(jis.pl) = %{tl_version}
Provides:       tex(jisn-v.pl) = %{tl_version}, tex(jisn.pl) = %{tl_version}
Provides:       tex(ngoth10.pl) = %{tl_version}, tex(ngoth5.pl) = %{tl_version}
Provides:       tex(ngoth6.pl) = %{tl_version}, tex(ngoth7.pl) = %{tl_version}
Provides:       tex(ngoth8.pl) = %{tl_version}, tex(ngoth9.pl) = %{tl_version}
Provides:       tex(nmin10.pl) = %{tl_version}, tex(nmin5.pl) = %{tl_version}
Provides:       tex(nmin6.pl) = %{tl_version}, tex(nmin7.pl) = %{tl_version}
Provides:       tex(nmin8.pl) = %{tl_version}, tex(nmin9.pl) = %{tl_version}
Provides:       tex(goth10.pl) = %{tl_version}, tex(goth5.pl) = %{tl_version}
Provides:       tex(goth6.pl) = %{tl_version}, tex(goth7.pl) = %{tl_version}
Provides:       tex(goth8.pl) = %{tl_version}, tex(goth9.pl) = %{tl_version}
Provides:       tex(min10.pl) = %{tl_version}, tex(min5.pl) = %{tl_version}
Provides:       tex(min6.pl) = %{tl_version}, tex(min7.pl) = %{tl_version}
Provides:       tex(min8.pl) = %{tl_version}, tex(min9.pl) = %{tl_version}
Provides:       tex(tgoth10.pl) = %{tl_version}, tex(tgoth5.pl) = %{tl_version}
Provides:       tex(tgoth6.pl) = %{tl_version}, tex(tgoth7.pl) = %{tl_version}
Provides:       tex(tgoth8.pl) = %{tl_version}, tex(tgoth9.pl) = %{tl_version}
Provides:       tex(tmin10.pl) = %{tl_version}, tex(tmin5.pl) = %{tl_version}
Provides:       tex(tmin6.pl) = %{tl_version}, tex(tmin7.pl) = %{tl_version}
Provides:       tex(tmin8.pl) = %{tl_version}, tex(tmin9.pl) = %{tl_version}
Provides:       tex(ascgrp.tfm) = %{tl_version}, tex(ascii10.tfm) = %{tl_version}
Provides:       tex(ascii36.tfm) = %{tl_version}, tex(gbm.tfm) = %{tl_version}
Provides:       tex(gbmv.tfm) = %{tl_version}, tex(rml.tfm) = %{tl_version}
Provides:       tex(rmlv.tfm) = %{tl_version}, tex(jis-v.tfm) = %{tl_version}
Provides:       tex(jis.tfm) = %{tl_version}, tex(jisg-v.tfm) = %{tl_version}
Provides:       tex(jisg.tfm) = %{tl_version}, tex(jisgn-v.tfm) = %{tl_version}
Provides:       tex(jisgn.tfm) = %{tl_version}, tex(jisn-v.tfm) = %{tl_version}
Provides:       tex(jisn.tfm) = %{tl_version}, tex(ngoth10.tfm) = %{tl_version}
Provides:       tex(ngoth5.tfm) = %{tl_version}, tex(ngoth6.tfm) = %{tl_version}
Provides:       tex(ngoth7.tfm) = %{tl_version}, tex(ngoth8.tfm) = %{tl_version}
Provides:       tex(ngoth9.tfm) = %{tl_version}, tex(nmin10.tfm) = %{tl_version}
Provides:       tex(nmin5.tfm) = %{tl_version}, tex(nmin6.tfm) = %{tl_version}
Provides:       tex(nmin7.tfm) = %{tl_version}, tex(nmin8.tfm) = %{tl_version}
Provides:       tex(nmin9.tfm) = %{tl_version}, tex(goth10.tfm) = %{tl_version}
Provides:       tex(goth5.tfm) = %{tl_version}, tex(goth6.tfm) = %{tl_version}
Provides:       tex(goth7.tfm) = %{tl_version}, tex(goth8.tfm) = %{tl_version}
Provides:       tex(goth9.tfm) = %{tl_version}, tex(min10.tfm) = %{tl_version}
Provides:       tex(min5.tfm) = %{tl_version}, tex(min6.tfm) = %{tl_version}
Provides:       tex(min7.tfm) = %{tl_version}, tex(min8.tfm) = %{tl_version}
Provides:       tex(min9.tfm) = %{tl_version}, tex(tgoth10.tfm) = %{tl_version}
Provides:       tex(tgoth5.tfm) = %{tl_version}, tex(tgoth6.tfm) = %{tl_version}
Provides:       tex(tgoth7.tfm) = %{tl_version}, tex(tgoth8.tfm) = %{tl_version}
Provides:       tex(tgoth9.tfm) = %{tl_version}, tex(tmin10.tfm) = %{tl_version}
Provides:       tex(tmin5.tfm) = %{tl_version}, tex(tmin6.tfm) = %{tl_version}
Provides:       tex(tmin7.tfm) = %{tl_version}, tex(tmin8.tfm) = %{tl_version}
Provides:       tex(tmin9.tfm) = %{tl_version}, tex(ascgrp.pfb) = %{tl_version}
Provides:       tex(ascii10.pfb) = %{tl_version}, tex(ascii36.pfb) = %{tl_version}
Provides:       tex(jis-v.vf) = %{tl_version}, tex(jis.vf) = %{tl_version}
Provides:       tex(jisg-v.vf) = %{tl_version}, tex(jisg.vf) = %{tl_version}
Provides:       tex(jisgn-v.vf) = %{tl_version}, tex(jisgn.vf) = %{tl_version}
Provides:       tex(jisn-v.vf) = %{tl_version}, tex(jisn.vf) = %{tl_version}
Provides:       tex(ngoth10.vf) = %{tl_version}, tex(ngoth5.vf) = %{tl_version}
Provides:       tex(ngoth6.vf) = %{tl_version}, tex(ngoth7.vf) = %{tl_version}
Provides:       tex(ngoth8.vf) = %{tl_version}, tex(ngoth9.vf) = %{tl_version}
Provides:       tex(nmin10.vf) = %{tl_version}, tex(nmin5.vf) = %{tl_version}
Provides:       tex(nmin6.vf) = %{tl_version}, tex(nmin7.vf) = %{tl_version}
Provides:       tex(nmin8.vf) = %{tl_version}, tex(nmin9.vf) = %{tl_version}
Provides:       tex(goth10.vf) = %{tl_version}, tex(goth5.vf) = %{tl_version}
Provides:       tex(goth6.vf) = %{tl_version}, tex(goth7.vf) = %{tl_version}
Provides:       tex(goth8.vf) = %{tl_version}, tex(goth9.vf) = %{tl_version}
Provides:       tex(min10.vf) = %{tl_version}, tex(min5.vf) = %{tl_version}
Provides:       tex(min6.vf) = %{tl_version}, tex(min7.vf) = %{tl_version}
Provides:       tex(min8.vf) = %{tl_version}, tex(min9.vf) = %{tl_version}
Provides:       tex(tgoth10.vf) = %{tl_version}, tex(tgoth5.vf) = %{tl_version}
Provides:       tex(tgoth6.vf) = %{tl_version}, tex(tgoth7.vf) = %{tl_version}
Provides:       tex(tgoth8.vf) = %{tl_version}, tex(tgoth9.vf) = %{tl_version}
Provides:       tex(tmin10.vf) = %{tl_version}, tex(tmin5.vf) = %{tl_version}
Provides:       tex(tmin6.vf) = %{tl_version}, tex(tmin7.vf) = %{tl_version}
Provides:       tex(tmin8.vf) = %{tl_version}, tex(tmin9.vf) = %{tl_version}

%description -n texlive-ptex-fonts
The bundle contains fonts for use with pTeX and the documents
for the makejvf program. This is a redistribution derived from
the ptex-texmf distribution by ASCII MEDIA WORKS.

%package -n texlive-ptex-fonts-doc
Summary:        Documentation for ptex-fonts
Version:        svn46940
Provides:       tex-ptex-fonts-doc
AutoReqProv:    No

%description -n texlive-ptex-fonts-doc
Documentation for ptex-fonts

%package -n texlive-ptex-base
Provides:       tex-ptex-base = %{tl_version}
License:        BSD
Summary:        Plain TeX format and documents for pTeX and e-pTeX
Version:        svn45140
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(ascii-jplain.tex) = %{tl_version}, tex(eptex.ini) = %{tl_version}
Provides:       tex(kinsoku.tex) = %{tl_version}, tex(ptex.ini) = %{tl_version}
Provides:       tex(ptex.tex) = %{tl_version}

%description -n texlive-ptex-base
The bundle contains plain TeX format and documents for pTeX and
e-pTeX.

%package -n texlive-ptex-base-doc
Summary:        Documentation for ptex-base
Version:        svn45140
Provides:       tex-ptex-base-doc
AutoReqProv:    No

%description -n texlive-ptex-base-doc
Documentation for ptex-base


%package -n texlive-pst-arrow
Summary:        special arrows for PSTricks
Version:        svn41980
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pst-arrow.tex) = %{tl_version}, tex(pst-arrow.sty) = %{tl_version}

%description -n texlive-pst-arrow
This package has all the code from the package pstricks-add
which was related to arrows, like multiple arrows and so on.

%package -n texlive-pst-geometrictools
Summary:        A PSTricks package to draw geometric tools
Version:        svn45319
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pst-geometrictools.tex) = %{tl_version}
Provides:       tex(pst-geometrictools.sty) = %{tl_version}

%description -n texlive-pst-geometrictools
This PSTricks package facilitates the drawing of protractors,
rulers, compasses and pencils.

%package -n texlive-pst-poker
Summary:        Drawing poker cards
Version:        svn48347
License:        LGPLv3
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pst-poker.sty) = %{tl_version}

%description -n texlive-pst-poker
This PSTricks related package can create poker cards in various
manners.

%package -n texlive-pstring
Summary:        typeset sequences with justification pointers
Version:        svn42857
License:        Public Domain
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pstring.sty) = %{tl_version}

%description -n texlive-pstring
This package lets you typeset justified sequences, also called
pointing strings. It's used for instance, in research papers
about Game Semantics to represent sequence of game moves with
their associated justification pointers. Depending on wether
using LaTeX or pdfLaTeX, the package uses PSTricks and pst-node
respectively pgf/TikZ.

%package -n texlive-pst-rputover
Summary:        Place text over objects without obscuring background colors
Version:        svn44724
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pst-rputover.tex) = %{tl_version}, tex(pst-rputover.sty) = %{tl_version}

%description -n texlive-pst-rputover
This is a PSTricks package which allows to place text over
objects without obscuring background colors.

%package -n texlive-pst-shell
Summary:        Plotting sea shells
Version:        svn42840
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pst-shell.tex) = %{tl_version}, tex(pst-shell.sty) = %{tl_version}
Requires:       texlive-pst-solides3d, texlive-pstricks

%description -n texlive-pst-shell
pst-shell is a PSTricks related package to draw seashells in 3D
view: Argonauta, Epiteonium, Lyria, Turritella, Tonna,
Achatina, Oxystele, Conus, Ammonite, Codakia, Escalaria,
Helcion, Natalina, Planorbis, and Nautilus, all with different
parameters. pst-shell needs pst-solides3d and an up-to-date
PSTricks, which should be part of your local TeX installation,
otherwise get it from a CTAN server.

%package -n texlive-pst-vehicle
Summary:        A PSTricks package for rolling vehicles on graphs of mathematical functions
Version:        svn45320
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(ListVehicles.tex) = %{tl_version}, tex(pst-vehicle.tex) = %{tl_version}
Provides:       tex(pst-vehicle.sty) = %{tl_version}

%description -n texlive-pst-vehicle
This package permits to represent vehicles rolling without
slipping on mathematical curves. Different types of vehicles
are proposed, the shape of the curve is to be defined by its
equation "y=f(x)" in algebraic notation.

%package -n texlive-pxtatescale
Summary:        Patch to graphics driver for scaling in vertical direction of pTeX
Version:        svn43009
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pxtatescale.sty) = %{tl_version}

%description -n texlive-pxtatescale
Patch for graphics driver 'dvipdfmx' to support correct scaling
in vertical direction of Japanese pTeX/upTeX.

%package -n texlive-pxufont
Summary:        Emulate non-Unicode Japanese fonts using Unicode fonts
Version:        svn44780
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(zu-brsgnmlgothb-h.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlgothb-v.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlgothbn-h.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlgothbn-v.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlgotheb-h.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlgotheb-v.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlgothebn-h.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlgothebn-v.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlgothr-h.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlgothr-v.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlgothrn-h.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlgothrn-v.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlmgothr-h.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlmgothr-v.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlmgothrn-h.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlmgothrn-v.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlminb-h.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlminb-v.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlminbn-h.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlminbn-v.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlminl-h.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlminl-v.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlminln-h.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlminln-v.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlminr-h.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlminr-v.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlminrn-h.tfm) = %{tl_version}
Provides:       tex(zu-brsgnmlminrn-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjgb0-h.tfm) = %{tl_version}, tex(zu-cidjgb0-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjgb1-h.tfm) = %{tl_version}, tex(zu-cidjgb1-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjgb2-h.tfm) = %{tl_version}, tex(zu-cidjgb2-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjgb3-h.tfm) = %{tl_version}, tex(zu-cidjgb3-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjgb4-h.tfm) = %{tl_version}, tex(zu-cidjgb4-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjgb5-h.tfm) = %{tl_version}, tex(zu-cidjgb5-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjge0-h.tfm) = %{tl_version}, tex(zu-cidjge0-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjge1-h.tfm) = %{tl_version}, tex(zu-cidjge1-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjge2-h.tfm) = %{tl_version}, tex(zu-cidjge2-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjge3-h.tfm) = %{tl_version}, tex(zu-cidjge3-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjge4-h.tfm) = %{tl_version}, tex(zu-cidjge4-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjge5-h.tfm) = %{tl_version}, tex(zu-cidjge5-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjgr0-h.tfm) = %{tl_version}, tex(zu-cidjgr0-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjgr1-h.tfm) = %{tl_version}, tex(zu-cidjgr1-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjgr2-h.tfm) = %{tl_version}, tex(zu-cidjgr2-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjgr3-h.tfm) = %{tl_version}, tex(zu-cidjgr3-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjgr4-h.tfm) = %{tl_version}, tex(zu-cidjgr4-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjgr5-h.tfm) = %{tl_version}, tex(zu-cidjgr5-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmb0-h.tfm) = %{tl_version}, tex(zu-cidjmb0-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmb1-h.tfm) = %{tl_version}, tex(zu-cidjmb1-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmb2-h.tfm) = %{tl_version}, tex(zu-cidjmb2-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmb3-h.tfm) = %{tl_version}, tex(zu-cidjmb3-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmb4-h.tfm) = %{tl_version}, tex(zu-cidjmb4-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmb5-h.tfm) = %{tl_version}, tex(zu-cidjmb5-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmgr0-h.tfm) = %{tl_version}, tex(zu-cidjmgr0-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmgr1-h.tfm) = %{tl_version}, tex(zu-cidjmgr1-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmgr2-h.tfm) = %{tl_version}, tex(zu-cidjmgr2-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmgr3-h.tfm) = %{tl_version}, tex(zu-cidjmgr3-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmgr4-h.tfm) = %{tl_version}, tex(zu-cidjmgr4-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmgr5-h.tfm) = %{tl_version}, tex(zu-cidjmgr5-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjml0-h.tfm) = %{tl_version}, tex(zu-cidjml0-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjml1-h.tfm) = %{tl_version}, tex(zu-cidjml1-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjml2-h.tfm) = %{tl_version}, tex(zu-cidjml2-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjml3-h.tfm) = %{tl_version}, tex(zu-cidjml3-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjml4-h.tfm) = %{tl_version}, tex(zu-cidjml4-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjml5-h.tfm) = %{tl_version}, tex(zu-cidjml5-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmr0-h.tfm) = %{tl_version}, tex(zu-cidjmr0-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmr1-h.tfm) = %{tl_version}, tex(zu-cidjmr1-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmr2-h.tfm) = %{tl_version}, tex(zu-cidjmr2-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmr3-h.tfm) = %{tl_version}, tex(zu-cidjmr3-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmr4-h.tfm) = %{tl_version}, tex(zu-cidjmr4-v.tfm) = %{tl_version}
Provides:       tex(zu-cidjmr5-h.tfm) = %{tl_version}, tex(zu-cidjmr5-v.tfm) = %{tl_version}
Provides:       tex(zu-jis-v.tfm) = %{tl_version}, tex(zu-jis.tfm) = %{tl_version}
Provides:       tex(zu-jisg-v.tfm) = %{tl_version}, tex(zu-jisg.tfm) = %{tl_version}
Provides:       tex(zu-nmlgothb-h.tfm) = %{tl_version}, tex(zu-nmlgothb-v.tfm) = %{tl_version}
Provides:       tex(zu-nmlgothbn-h.tfm) = %{tl_version}, tex(zu-nmlgothbn-v.tfm) = %{tl_version}
Provides:       tex(zu-nmlgotheb-h.tfm) = %{tl_version}, tex(zu-nmlgotheb-v.tfm) = %{tl_version}
Provides:       tex(zu-nmlgothebn-h.tfm) = %{tl_version}
Provides:       tex(zu-nmlgothebn-v.tfm) = %{tl_version}
Provides:       tex(zu-nmlgothr-h.tfm) = %{tl_version}, tex(zu-nmlgothr-v.tfm) = %{tl_version}
Provides:       tex(zu-nmlgothrn-h.tfm) = %{tl_version}, tex(zu-nmlgothrn-v.tfm) = %{tl_version}
Provides:       tex(zu-nmlmgothr-h.tfm) = %{tl_version}, tex(zu-nmlmgothr-v.tfm) = %{tl_version}
Provides:       tex(zu-nmlmgothrn-h.tfm) = %{tl_version}
Provides:       tex(zu-nmlmgothrn-v.tfm) = %{tl_version}
Provides:       tex(zu-nmlminb-h.tfm) = %{tl_version}, tex(zu-nmlminb-v.tfm) = %{tl_version}
Provides:       tex(zu-nmlminbn-h.tfm) = %{tl_version}, tex(zu-nmlminbn-v.tfm) = %{tl_version}
Provides:       tex(zu-nmlminl-h.tfm) = %{tl_version}, tex(zu-nmlminl-v.tfm) = %{tl_version}
Provides:       tex(zu-nmlminln-h.tfm) = %{tl_version}, tex(zu-nmlminln-v.tfm) = %{tl_version}
Provides:       tex(zu-nmlminr-h.tfm) = %{tl_version}, tex(zu-nmlminr-v.tfm) = %{tl_version}
Provides:       tex(zu-nmlminrn-h.tfm) = %{tl_version}, tex(zu-nmlminrn-v.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothb-h.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothb-v.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothbn-h.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothbn-v.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgotheb-h.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgotheb-v.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothebn-h.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothebn-v.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothr-h.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothr-v.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothrn-h.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothrn-v.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlmgothr-h.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlmgothr-v.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlmgothrn-h.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlmgothrn-v.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminb-h.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminb-v.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminbn-h.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminbn-v.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminl-h.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminl-v.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminln-h.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminln-v.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminr-h.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminr-v.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminrn-h.tfm) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminrn-v.tfm) = %{tl_version}
Provides:       tex(zu-upnmlgothb-h.tfm) = %{tl_version}
Provides:       tex(zu-upnmlgothb-v.tfm) = %{tl_version}
Provides:       tex(zu-upnmlgothbn-h.tfm) = %{tl_version}
Provides:       tex(zu-upnmlgothbn-v.tfm) = %{tl_version}
Provides:       tex(zu-upnmlgotheb-h.tfm) = %{tl_version}
Provides:       tex(zu-upnmlgotheb-v.tfm) = %{tl_version}
Provides:       tex(zu-upnmlgothebn-h.tfm) = %{tl_version}
Provides:       tex(zu-upnmlgothebn-v.tfm) = %{tl_version}
Provides:       tex(zu-upnmlgothr-h.tfm) = %{tl_version}
Provides:       tex(zu-upnmlgothr-v.tfm) = %{tl_version}
Provides:       tex(zu-upnmlgothrn-h.tfm) = %{tl_version}
Provides:       tex(zu-upnmlgothrn-v.tfm) = %{tl_version}
Provides:       tex(zu-upnmlmgothr-h.tfm) = %{tl_version}
Provides:       tex(zu-upnmlmgothr-v.tfm) = %{tl_version}
Provides:       tex(zu-upnmlmgothrn-h.tfm) = %{tl_version}
Provides:       tex(zu-upnmlmgothrn-v.tfm) = %{tl_version}
Provides:       tex(zu-upnmlminb-h.tfm) = %{tl_version}, tex(zu-upnmlminb-v.tfm) = %{tl_version}
Provides:       tex(zu-upnmlminbn-h.tfm) = %{tl_version}
Provides:       tex(zu-upnmlminbn-v.tfm) = %{tl_version}
Provides:       tex(zu-upnmlminl-h.tfm) = %{tl_version}, tex(zu-upnmlminl-v.tfm) = %{tl_version}
Provides:       tex(zu-upnmlminln-h.tfm) = %{tl_version}
Provides:       tex(zu-upnmlminln-v.tfm) = %{tl_version}
Provides:       tex(zu-upnmlminr-h.tfm) = %{tl_version}, tex(zu-upnmlminr-v.tfm) = %{tl_version}
Provides:       tex(zu-upnmlminrn-h.tfm) = %{tl_version}
Provides:       tex(zu-upnmlminrn-v.tfm) = %{tl_version}
Provides:       tex(pxufont.sty) = %{tl_version}, tex(zu-brsgnmlgothb-h.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlgothb-v.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlgothbn-h.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlgothbn-v.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlgotheb-h.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlgotheb-v.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlgothebn-h.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlgothebn-v.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlgothr-h.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlgothr-v.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlgothrn-h.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlgothrn-v.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlmgothr-h.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlmgothr-v.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlmgothrn-h.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlmgothrn-v.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlminb-h.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlminb-v.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlminbn-h.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlminbn-v.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlminl-h.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlminl-v.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlminln-h.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlminln-v.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlminr-h.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlminr-v.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlminrn-h.vf) = %{tl_version}
Provides:       tex(zu-brsgnmlminrn-v.vf) = %{tl_version}
Provides:       tex(zu-cidjgb0-h.vf) = %{tl_version}, tex(zu-cidjgb0-v.vf) = %{tl_version}
Provides:       tex(zu-cidjgb1-h.vf) = %{tl_version}, tex(zu-cidjgb1-v.vf) = %{tl_version}
Provides:       tex(zu-cidjgb2-h.vf) = %{tl_version}, tex(zu-cidjgb2-v.vf) = %{tl_version}
Provides:       tex(zu-cidjgb3-h.vf) = %{tl_version}, tex(zu-cidjgb3-v.vf) = %{tl_version}
Provides:       tex(zu-cidjgb4-h.vf) = %{tl_version}, tex(zu-cidjgb4-v.vf) = %{tl_version}
Provides:       tex(zu-cidjgb5-h.vf) = %{tl_version}, tex(zu-cidjgb5-v.vf) = %{tl_version}
Provides:       tex(zu-cidjge0-h.vf) = %{tl_version}, tex(zu-cidjge0-v.vf) = %{tl_version}
Provides:       tex(zu-cidjge1-h.vf) = %{tl_version}, tex(zu-cidjge1-v.vf) = %{tl_version}
Provides:       tex(zu-cidjge2-h.vf) = %{tl_version}, tex(zu-cidjge2-v.vf) = %{tl_version}
Provides:       tex(zu-cidjge3-h.vf) = %{tl_version}, tex(zu-cidjge3-v.vf) = %{tl_version}
Provides:       tex(zu-cidjge4-h.vf) = %{tl_version}, tex(zu-cidjge4-v.vf) = %{tl_version}
Provides:       tex(zu-cidjge5-h.vf) = %{tl_version}, tex(zu-cidjge5-v.vf) = %{tl_version}
Provides:       tex(zu-cidjgr0-h.vf) = %{tl_version}, tex(zu-cidjgr0-v.vf) = %{tl_version}
Provides:       tex(zu-cidjgr1-h.vf) = %{tl_version}, tex(zu-cidjgr1-v.vf) = %{tl_version}
Provides:       tex(zu-cidjgr2-h.vf) = %{tl_version}, tex(zu-cidjgr2-v.vf) = %{tl_version}
Provides:       tex(zu-cidjgr3-h.vf) = %{tl_version}, tex(zu-cidjgr3-v.vf) = %{tl_version}
Provides:       tex(zu-cidjgr4-h.vf) = %{tl_version}, tex(zu-cidjgr4-v.vf) = %{tl_version}
Provides:       tex(zu-cidjgr5-h.vf) = %{tl_version}, tex(zu-cidjgr5-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmb0-h.vf) = %{tl_version}, tex(zu-cidjmb0-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmb1-h.vf) = %{tl_version}, tex(zu-cidjmb1-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmb2-h.vf) = %{tl_version}, tex(zu-cidjmb2-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmb3-h.vf) = %{tl_version}, tex(zu-cidjmb3-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmb4-h.vf) = %{tl_version}, tex(zu-cidjmb4-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmb5-h.vf) = %{tl_version}, tex(zu-cidjmb5-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmgr0-h.vf) = %{tl_version}, tex(zu-cidjmgr0-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmgr1-h.vf) = %{tl_version}, tex(zu-cidjmgr1-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmgr2-h.vf) = %{tl_version}, tex(zu-cidjmgr2-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmgr3-h.vf) = %{tl_version}, tex(zu-cidjmgr3-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmgr4-h.vf) = %{tl_version}, tex(zu-cidjmgr4-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmgr5-h.vf) = %{tl_version}, tex(zu-cidjmgr5-v.vf) = %{tl_version}
Provides:       tex(zu-cidjml0-h.vf) = %{tl_version}, tex(zu-cidjml0-v.vf) = %{tl_version}
Provides:       tex(zu-cidjml1-h.vf) = %{tl_version}, tex(zu-cidjml1-v.vf) = %{tl_version}
Provides:       tex(zu-cidjml2-h.vf) = %{tl_version}, tex(zu-cidjml2-v.vf) = %{tl_version}
Provides:       tex(zu-cidjml3-h.vf) = %{tl_version}, tex(zu-cidjml3-v.vf) = %{tl_version}
Provides:       tex(zu-cidjml4-h.vf) = %{tl_version}, tex(zu-cidjml4-v.vf) = %{tl_version}
Provides:       tex(zu-cidjml5-h.vf) = %{tl_version}, tex(zu-cidjml5-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmr0-h.vf) = %{tl_version}, tex(zu-cidjmr0-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmr1-h.vf) = %{tl_version}, tex(zu-cidjmr1-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmr2-h.vf) = %{tl_version}, tex(zu-cidjmr2-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmr3-h.vf) = %{tl_version}, tex(zu-cidjmr3-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmr4-h.vf) = %{tl_version}, tex(zu-cidjmr4-v.vf) = %{tl_version}
Provides:       tex(zu-cidjmr5-h.vf) = %{tl_version}, tex(zu-cidjmr5-v.vf) = %{tl_version}
Provides:       tex(zu-jis-v.vf) = %{tl_version}, tex(zu-jis.vf) = %{tl_version}
Provides:       tex(zu-jisg-v.vf) = %{tl_version}, tex(zu-jisg.vf) = %{tl_version}
Provides:       tex(zu-nmlgothb-h.vf) = %{tl_version}, tex(zu-nmlgothb-v.vf) = %{tl_version}
Provides:       tex(zu-nmlgothbn-h.vf) = %{tl_version}, tex(zu-nmlgothbn-v.vf) = %{tl_version}
Provides:       tex(zu-nmlgotheb-h.vf) = %{tl_version}, tex(zu-nmlgotheb-v.vf) = %{tl_version}
Provides:       tex(zu-nmlgothebn-h.vf) = %{tl_version}, tex(zu-nmlgothebn-v.vf) = %{tl_version}
Provides:       tex(zu-nmlgothr-h.vf) = %{tl_version}, tex(zu-nmlgothr-v.vf) = %{tl_version}
Provides:       tex(zu-nmlgothrn-h.vf) = %{tl_version}, tex(zu-nmlgothrn-v.vf) = %{tl_version}
Provides:       tex(zu-nmlmgothr-h.vf) = %{tl_version}, tex(zu-nmlmgothr-v.vf) = %{tl_version}
Provides:       tex(zu-nmlmgothrn-h.vf) = %{tl_version}, tex(zu-nmlmgothrn-v.vf) = %{tl_version}
Provides:       tex(zu-nmlminb-h.vf) = %{tl_version}, tex(zu-nmlminb-v.vf) = %{tl_version}
Provides:       tex(zu-nmlminbn-h.vf) = %{tl_version}, tex(zu-nmlminbn-v.vf) = %{tl_version}
Provides:       tex(zu-nmlminl-h.vf) = %{tl_version}, tex(zu-nmlminl-v.vf) = %{tl_version}
Provides:       tex(zu-nmlminln-h.vf) = %{tl_version}, tex(zu-nmlminln-v.vf) = %{tl_version}
Provides:       tex(zu-nmlminr-h.vf) = %{tl_version}, tex(zu-nmlminr-v.vf) = %{tl_version}
Provides:       tex(zu-nmlminrn-h.vf) = %{tl_version}, tex(zu-nmlminrn-v.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothb-h.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothb-v.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothbn-h.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothbn-v.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgotheb-h.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgotheb-v.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothebn-h.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothebn-v.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothr-h.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothr-v.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothrn-h.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlgothrn-v.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlmgothr-h.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlmgothr-v.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlmgothrn-h.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlmgothrn-v.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminb-h.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminb-v.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminbn-h.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminbn-v.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminl-h.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminl-v.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminln-h.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminln-v.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminr-h.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminr-v.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminrn-h.vf) = %{tl_version}
Provides:       tex(zu-upbrsgnmlminrn-v.vf) = %{tl_version}
Provides:       tex(zu-upnmlgothb-h.vf) = %{tl_version}, tex(zu-upnmlgothb-v.vf) = %{tl_version}
Provides:       tex(zu-upnmlgothbn-h.vf) = %{tl_version}
Provides:       tex(zu-upnmlgothbn-v.vf) = %{tl_version}
Provides:       tex(zu-upnmlgotheb-h.vf) = %{tl_version}
Provides:       tex(zu-upnmlgotheb-v.vf) = %{tl_version}
Provides:       tex(zu-upnmlgothebn-h.vf) = %{tl_version}
Provides:       tex(zu-upnmlgothebn-v.vf) = %{tl_version}
Provides:       tex(zu-upnmlgothr-h.vf) = %{tl_version}, tex(zu-upnmlgothr-v.vf) = %{tl_version}
Provides:       tex(zu-upnmlgothrn-h.vf) = %{tl_version}
Provides:       tex(zu-upnmlgothrn-v.vf) = %{tl_version}
Provides:       tex(zu-upnmlmgothr-h.vf) = %{tl_version}
Provides:       tex(zu-upnmlmgothr-v.vf) = %{tl_version}
Provides:       tex(zu-upnmlmgothrn-h.vf) = %{tl_version}
Provides:       tex(zu-upnmlmgothrn-v.vf) = %{tl_version}
Provides:       tex(zu-upnmlminb-h.vf) = %{tl_version}, tex(zu-upnmlminb-v.vf) = %{tl_version}
Provides:       tex(zu-upnmlminbn-h.vf) = %{tl_version}, tex(zu-upnmlminbn-v.vf) = %{tl_version}
Provides:       tex(zu-upnmlminl-h.vf) = %{tl_version}, tex(zu-upnmlminl-v.vf) = %{tl_version}
Provides:       tex(zu-upnmlminln-h.vf) = %{tl_version}, tex(zu-upnmlminln-v.vf) = %{tl_version}
Provides:       tex(zu-upnmlminr-h.vf) = %{tl_version}, tex(zu-upnmlminr-v.vf) = %{tl_version}
Provides:       tex(zu-upnmlminrn-h.vf) = %{tl_version}, tex(zu-upnmlminrn-v.vf) = %{tl_version}

%description -n texlive-pxufont
The set of the Japanese logical fonts (JFMs) that are used as
standard fonts in pTeX and upTeX contains both Unicode JFMs and
non-Unicode JFMs. This bundle provides an alternative set of
non-Unicode JFMs that are tied to the virtual fonts (VFs) that
refer to the glyphs in the Unicode JFMs. Moreover it provides a
LaTeX package that redefines the NFSS settings of the Japanese
fonts of (u)pLaTeX so that the new set of non-Unicode JFMs will
be employed. As a whole, this bundle allows users to dispense
with the mapping setup on non-Unicode JFMs. Such a setup is
useful in particular when users want to use OpenType fonts
(such as Source Han Serif) that have a glyph encoding different
from Adobe-Japan1, because mapping setups from non-Unicode JFMs
to such physical fonts are difficult to prepare.

%package -n texlive-pst-antiprism
Summary:        A PSTricks related package which draws an antiprism
Version:        svn46643
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pst-antiprism.pro) = %{tl_version}, tex(pst-antiprism.tex) = %{tl_version}
Provides:       tex(pst-antiprism.sty) = %{tl_version}

%description -n texlive-pst-antiprism
pst-antiprism is a PSTricks related package which draws an
antiprism, which is a semiregular polyhedron constructed with
2-gons and triangles.

%package -n texlive-pst-calculate
Summary:        Support for floating point operations at LaTeX level
Version:        svn46544
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(expl3.sty)
Requires:       tex(siunitx.sty), tex(xkeyval.sty), tex(xparse.sty)
Provides:       tex(pst-calculate.sty) = %{tl_version}

%description -n texlive-pst-calculate
This package provides an interface to the LaTeX3 floating point
unit (part of expl3), mainly used for PSTricks related packages
to allow math expressions at LaTeX level. siunitx is used for
formatting the calculated number. The package also depends on
xkeyval and xparse.

%package -n texlive-pst-contourplot
Summary:        Draw implicit functions using the "marching squares" algorithm
Version:        svn48230
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pst-contourplot.tex) = %{tl_version}
Provides:       tex(pst-contourplot.sty) = %{tl_version}

%description -n texlive-pst-contourplot
This package allows to draw implicit functions "f(x,y) = 0"
with options for coloring the inside of the surfaces, for
marking the points and arrowing the curve at points chosen by
the user. The package uses the "marching squares" algorithm.

%package -n texlive-pst-dart
Summary:        Plotting dart boards
Version:        svn46579
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pst-dart.sty) = %{tl_version}, tex(pst-dart.tex) = %{tl_version}

%description -n texlive-pst-dart
pst-dart is a PSTricks related package and draws Dart Boards.
Optional arguments are the unit and the fontsize.

%package -n texlive-pst-spinner
Summary:        Drawing a fidget spinner
Version:        svn44507
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pst-spinner.sty) = %{tl_version}, tex(pst-spinner.tex) = %{tl_version}

%description -n texlive-pst-spinner
This package aims to propose a model of the fidget spinner
gadget. It exists under different forms with 2, 3 poles and
even more. We chose the most popular model: the triple Fidget
Spinner. You can run the PSTricks related documents with
XeLaTeX.

%package -n texlive-pythonhighlight
Summary:        Highlighting of Python code, based on the listings package
Version:        svn43191
License:        BSD
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pythonhighlight.sty) = %{tl_version}

%description -n texlive-pythonhighlight
Highlighting of Python code, based on the listings package.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="public/punknova"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
cp -R %{buildroot}/%{_texdir}/texmf-dist/doc/man %{buildroot}/%{_datadir}/
rm -f %{buildroot}%{_datadir}/man/man5/prerex.man5.pdf*
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/doc/man/man5/prerex.*
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-pslatex
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/pslatex/
%{_texdir}/texmf-dist/fonts/tfm/public/pslatex/
%{_texdir}/texmf-dist/fonts/vf/public/pslatex/
%{_texdir}/texmf-dist/tex/latex/pslatex/

%files -n texlive-psnfss
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/psnfss/
%{_texdir}/texmf-dist/tex/latex/psnfss/

%files -n texlive-psnfss-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/psnfss/

%files -n texlive-pspicture
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pspicture/
%{_texdir}/texmf-dist/tex/latex/pspicture/

%files -n texlive-pspicture-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pspicture/

%files -n texlive-psizzl
%license lppl1.txt
%{_texdir}/texmf-dist/tex/psizzl/

%files -n texlive-psizzl-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/otherformats/psizzl/

%files -n texlive-pxcjkcat
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/pxcjkcat/

%files -n texlive-pxcjkcat-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/pxcjkcat/

%files -n texlive-pxjahyper
%license other-free.txt
%{_texdir}/texmf-dist/tex/platex/pxjahyper/

%files -n texlive-pxjahyper-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/platex/pxjahyper/

%files -n texlive-pxrubrica
%{_texdir}/texmf-dist/tex/platex/pxrubrica/

%files -n texlive-pxrubrica-doc
%{_texdir}/texmf-dist/doc/platex/pxrubrica/

%files -n texlive-pxfonts
%license gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/
%{_texdir}/texmf-dist/fonts/map/dvips/pxfonts/
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/
%{_texdir}/texmf-dist/tex/latex/pxfonts/

%files -n texlive-pxfonts-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/pxfonts/

%files -n texlive-prodint
%{_texdir}/texmf-dist/fonts/afm/public/prodint/
%{_texdir}/texmf-dist/fonts/map/dvips/prodint/
%{_texdir}/texmf-dist/fonts/tfm/public/prodint/
%{_texdir}/texmf-dist/fonts/type1/public/prodint/
%{_texdir}/texmf-dist/tex/latex/prodint/

%files -n texlive-prodint-doc
%{_texdir}/texmf-dist/doc/fonts/prodint/

%files -n texlive-punk
%license knuth.txt
%{_texdir}/texmf-dist/fonts/source/public/punk/
%{_texdir}/texmf-dist/fonts/tfm/public/punk/

%files -n texlive-punk-doc
%license knuth.txt
%{_texdir}/texmf-dist/doc/fonts/punk/

%files -n texlive-punk-latex
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/punk-latex/

%files -n texlive-punk-latex-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/punk-latex/

%files -n texlive-punknova
%{_datadir}/fonts/punknova
%{_texdir}/texmf-dist/fonts/opentype/public/punknova/

%files -n texlive-punknova-doc
%{_texdir}/texmf-dist/doc/fonts/punknova/

%files -n texlive-pxtxalfa
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/pxtxalfa/
%{_texdir}/texmf-dist/fonts/tfm/public/pxtxalfa/
%{_texdir}/texmf-dist/fonts/vf/public/pxtxalfa/
%{_texdir}/texmf-dist/tex/latex/pxtxalfa/

%files -n texlive-pxtxalfa-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/pxtxalfa/

%files -n texlive-psgo
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/psgo/

%files -n texlive-psgo-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/psgo/

%files -n texlive-pst-eucl-translation-bg-doc
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/

%files -n texlive-presentations-en-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/presentations-en/

%files -n texlive-presentations-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/presentations/

%files -n texlive-przechlewski-book
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/przechlewski-book/
%{_texdir}/texmf-dist/tex/latex/przechlewski-book/

%files -n texlive-przechlewski-book-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/przechlewski-book/

%files -n texlive-pxchfon
%license other-free.txt
%{_texdir}/texmf-dist/fonts/sfd/pxchfon/
%{_texdir}/texmf-dist/fonts/tfm/public/pxchfon/
%{_texdir}/texmf-dist/fonts/vf/public/pxchfon/
%{_texdir}/texmf-dist/tex/platex/pxchfon/

%files -n texlive-pxchfon-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/platex/pxchfon/

%files -n texlive-pxbase
%license other-free.txt
%{_texdir}/texmf-dist/tex/platex/pxbase/

%files -n texlive-pxbase-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/platex/pxbase/

%files -n texlive-psfrag
%{_texdir}/texmf-dist/dvips/psfrag/
%{_texdir}/texmf-dist/tex/latex/psfrag/

%files -n texlive-psfrag-doc
%{_texdir}/texmf-dist/doc/latex/psfrag/

%files -n texlive-psfrag-italian-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/psfrag-italian/

%files -n texlive-prerex
%license gpl.txt
%{_mandir}/man5/prerex.5*
%{_texdir}/texmf-dist/tex/latex/prerex/

%files -n texlive-prerex-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/prerex/

%files -n texlive-productbox
%{_texdir}/texmf-dist/tex/latex/productbox/

%files -n texlive-productbox-doc
%{_texdir}/texmf-dist/doc/latex/productbox/

%files -n texlive-pxpgfmark
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/pxpgfmark/

%files -n texlive-pxpgfmark-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/pxpgfmark/

%files -n texlive-preprint
%license collection.txt
%{_texdir}/texmf-dist/tex/latex/preprint/

%files -n texlive-preprint-doc
%license collection.txt
%{_texdir}/texmf-dist/doc/latex/preprint/

%files -n texlive-pressrelease
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/pressrelease/

%files -n texlive-pressrelease-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/pressrelease/

%files -n texlive-prettyref
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/prettyref/

%files -n texlive-prettyref-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/prettyref/

%files -n texlive-printlen
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/printlen/

%files -n texlive-printlen-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/printlen/

%files -n texlive-probsoln
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/probsoln/

%files -n texlive-probsoln-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/probsoln/

%files -n texlive-program
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/program/

%files -n texlive-program-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/program/

%files -n texlive-progress
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/progress/

%files -n texlive-progress-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/progress/

%files -n texlive-progressbar
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/progressbar/

%files -n texlive-progressbar-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/progressbar/

%files -n texlive-proofread
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/proofread/

%files -n texlive-proofread-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/proofread/

%files -n texlive-properties
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/properties/

%files -n texlive-properties-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/properties/

%files -n texlive-prosper
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/prosper/

%files -n texlive-prosper-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/prosper/

%files -n texlive-protex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/protex/

%files -n texlive-protex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/protex/

%files -n texlive-protocol
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/protocol/

%files -n texlive-protocol-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/protocol/

%files -n texlive-psfragx
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/psfragx/

%files -n texlive-psfragx-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/psfragx/

%files -n texlive-pstool
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pstool/

%files -n texlive-pstool-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pstool/

%files -n texlive-pxgreeks
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/pxgreeks/

%files -n texlive-pxgreeks-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/pxgreeks/

%files -n texlive-python
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/python/

%files -n texlive-python-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/python/

%files -n texlive-prftree
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/prftree/

%files -n texlive-prftree-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/prftree/

%files -n texlive-proba
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/proba/

%files -n texlive-proba-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/proba/

%files -n texlive-present
%license lppl1.txt
%{_texdir}/texmf-dist/tex/plain/present/

%files -n texlive-present-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/plain/present/


%files -n texlive-psbao
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/psbao/

%files -n texlive-psbao-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/psbao/

%files -n texlive-pst-2dplot
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pst-2dplot/

%files -n texlive-pst-2dplot-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-2dplot/

%files -n texlive-pst-3d
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-3d/
%{_texdir}/texmf-dist/tex/generic/pst-3d/
%{_texdir}/texmf-dist/tex/latex/pst-3d/

%files -n texlive-pst-3d-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-3d/

%files -n texlive-pst-3dplot
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-3dplot/
%{_texdir}/texmf-dist/tex/generic/pst-3dplot/
%{_texdir}/texmf-dist/tex/latex/pst-3dplot/

%files -n texlive-pst-3dplot-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-3dplot/

%files -n texlive-pst-abspos
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-abspos/
%{_texdir}/texmf-dist/tex/latex/pst-abspos/

%files -n texlive-pst-abspos-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-abspos/

%files -n texlive-pst-am
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pst-am/

%files -n texlive-pst-am-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-am/

%files -n texlive-pst-asr
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-asr/
%{_texdir}/texmf-dist/tex/latex/pst-asr/

%files -n texlive-pst-asr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-asr/

%files -n texlive-pst-bar
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-bar/
%{_texdir}/texmf-dist/tex/generic/pst-bar/
%{_texdir}/texmf-dist/tex/latex/pst-bar/

%files -n texlive-pst-bar-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-bar/

%files -n texlive-pst-barcode
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-barcode/
%{_texdir}/texmf-dist/tex/generic/pst-barcode/
%{_texdir}/texmf-dist/tex/latex/pst-barcode/

%files -n texlive-pst-barcode-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-barcode/

%files -n texlive-pst-bezier
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-bezier/
%{_texdir}/texmf-dist/tex/generic/pst-bezier/
%{_texdir}/texmf-dist/tex/latex/pst-bezier/

%files -n texlive-pst-bezier-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-bezier/

%files -n texlive-pst-blur
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-blur/
%{_texdir}/texmf-dist/tex/generic/pst-blur/
%{_texdir}/texmf-dist/tex/latex/pst-blur/

%files -n texlive-pst-blur-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-blur/

%files -n texlive-pst-bspline
%{_texdir}/texmf-dist/dvips/pst-bspline/
%{_texdir}/texmf-dist/tex/generic/pst-bspline/
%{_texdir}/texmf-dist/tex/latex/pst-bspline/

%files -n texlive-pst-bspline-doc
%{_texdir}/texmf-dist/doc/generic/pst-bspline/

%files -n texlive-pst-calendar
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pst-calendar/

%files -n texlive-pst-calendar-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pst-calendar/

%files -n texlive-pst-circ
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-circ/
%{_texdir}/texmf-dist/tex/generic/pst-circ/
%{_texdir}/texmf-dist/tex/latex/pst-circ/

%files -n texlive-pst-circ-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-circ/

%files -n texlive-pst-coil
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-coil/
%{_texdir}/texmf-dist/tex/generic/pst-coil/
%{_texdir}/texmf-dist/tex/latex/pst-coil/

%files -n texlive-pst-coil-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-coil/

%files -n texlive-pst-cox
%license lgpl2.1.txt
%{_texdir}/texmf-dist/dvips/pst-cox/
%{_texdir}/texmf-dist/tex/generic/pst-cox/
%{_texdir}/texmf-dist/tex/latex/pst-cox/

%files -n texlive-pst-cox-doc
%license lgpl2.1.txt
%{_texdir}/texmf-dist/doc/generic/pst-cox/

%files -n texlive-pst-dbicons
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pst-dbicons/

%files -n texlive-pst-dbicons-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-dbicons/

%files -n texlive-pst-diffraction
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-diffraction/
%{_texdir}/texmf-dist/tex/latex/pst-diffraction/

%files -n texlive-pst-diffraction-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-diffraction/

%files -n texlive-pst-electricfield
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-electricfield/
%{_texdir}/texmf-dist/tex/generic/pst-electricfield/
%{_texdir}/texmf-dist/tex/latex/pst-electricfield/

%files -n texlive-pst-electricfield-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-electricfield/

%files -n texlive-pst-eps
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-eps/
%{_texdir}/texmf-dist/tex/latex/pst-eps/

%files -n texlive-pst-eps-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-eps/

%files -n texlive-pst-eucl
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-eucl/
%{_texdir}/texmf-dist/tex/generic/pst-eucl/
%{_texdir}/texmf-dist/tex/latex/pst-eucl/

%files -n texlive-pst-eucl-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-eucl/

%files -n texlive-pst-exa
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pst-exa/

%files -n texlive-pst-exa-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pst-exa/

%files -n texlive-pst-fill
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-fill/
%{_texdir}/texmf-dist/tex/latex/pst-fill/

%files -n texlive-pst-fill-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-fill/

%files -n texlive-pst-fit
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-fit/
%{_texdir}/texmf-dist/tex/latex/pst-fit/

%files -n texlive-pst-fit-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-fit/

%files -n texlive-pst-fr3d
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-fr3d/
%{_texdir}/texmf-dist/tex/latex/pst-fr3d/

%files -n texlive-pst-fr3d-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-fr3d/

%files -n texlive-pst-fractal
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-fractal/
%{_texdir}/texmf-dist/tex/generic/pst-fractal/
%{_texdir}/texmf-dist/tex/latex/pst-fractal/

%files -n texlive-pst-fractal-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-fractal/

%files -n texlive-pst-fun
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-fun/
%{_texdir}/texmf-dist/tex/generic/pst-fun/
%{_texdir}/texmf-dist/tex/latex/pst-fun/

%files -n texlive-pst-fun-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-fun/

%files -n texlive-pst-func
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-func/
%{_texdir}/texmf-dist/tex/generic/pst-func/
%{_texdir}/texmf-dist/tex/latex/pst-func/

%files -n texlive-pst-func-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-func/

%files -n texlive-pst-gantt
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-gantt/
%{_texdir}/texmf-dist/tex/latex/pst-gantt/

%files -n texlive-pst-gantt-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-gantt/

%files -n texlive-pst-geo
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-geo/
%{_texdir}/texmf-dist/tex/generic/pst-geo/
%{_texdir}/texmf-dist/tex/latex/pst-geo/

%files -n texlive-pst-geo-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-geo/

%files -n texlive-pst-ghsb
%{_texdir}/texmf-dist/dvips/pst-ghsb/
%{_texdir}/texmf-dist/tex/generic/pst-ghsb/
%{_texdir}/texmf-dist/tex/latex/pst-ghsb/

%files -n texlive-pst-ghsb-doc
%{_texdir}/texmf-dist/doc/generic/pst-ghsb/

%files -n texlive-pst-gr3d
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-gr3d/
%{_texdir}/texmf-dist/tex/latex/pst-gr3d/

%files -n texlive-pst-gr3d-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-gr3d/

%files -n texlive-pst-grad
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-grad/
%{_texdir}/texmf-dist/tex/generic/pst-grad/
%{_texdir}/texmf-dist/tex/latex/pst-grad/

%files -n texlive-pst-grad-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-grad/

%files -n texlive-pst-graphicx
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-graphicx/

%files -n texlive-pst-graphicx-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-graphicx/

%files -n texlive-pst-infixplot
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-infixplot/
%{_texdir}/texmf-dist/tex/latex/pst-infixplot/

%files -n texlive-pst-infixplot-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-infixplot/

%files -n texlive-pst-intersect
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-intersect/
%{_texdir}/texmf-dist/tex/generic/pst-intersect/
%{_texdir}/texmf-dist/tex/latex/pst-intersect/

%files -n texlive-pst-intersect-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pst-intersect/

%files -n texlive-pst-jtree
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/pst-jtree/
%{_texdir}/texmf-dist/tex/latex/pst-jtree/

%files -n texlive-pst-jtree-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/pst-jtree/

%files -n texlive-pst-knot
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-knot/
%{_texdir}/texmf-dist/tex/generic/pst-knot/
%{_texdir}/texmf-dist/tex/latex/pst-knot/

%files -n texlive-pst-knot-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-knot/

%files -n texlive-pst-labo
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-labo/
%{_texdir}/texmf-dist/tex/latex/pst-labo/

%files -n texlive-pst-labo-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-labo/

%files -n texlive-pst-layout
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pst-layout/

%files -n texlive-pst-layout-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pst-layout/

%files -n texlive-pst-lens
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-lens/
%{_texdir}/texmf-dist/tex/latex/pst-lens/

%files -n texlive-pst-lens-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-lens/

%files -n texlive-pst-light3d
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-light3d/
%{_texdir}/texmf-dist/tex/generic/pst-light3d/
%{_texdir}/texmf-dist/tex/latex/pst-light3d/

%files -n texlive-pst-light3d-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-light3d/

%files -n texlive-pst-magneticfield
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-magneticfield/
%{_texdir}/texmf-dist/tex/generic/pst-magneticfield/
%{_texdir}/texmf-dist/tex/latex/pst-magneticfield/

%files -n texlive-pst-magneticfield-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-magneticfield/

%files -n texlive-pst-math
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-math/
%{_texdir}/texmf-dist/tex/generic/pst-math/
%{_texdir}/texmf-dist/tex/latex/pst-math/

%files -n texlive-pst-math-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-math/

%files -n texlive-pst-mirror
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-mirror/
%{_texdir}/texmf-dist/tex/generic/pst-mirror/
%{_texdir}/texmf-dist/tex/latex/pst-mirror/

%files -n texlive-pst-mirror-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-mirror/

%files -n texlive-pst-node
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-node/
%{_texdir}/texmf-dist/tex/generic/pst-node/
%{_texdir}/texmf-dist/tex/latex/pst-node/

%files -n texlive-pst-node-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-node/

%files -n texlive-pst-ob3d
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-ob3d/
%{_texdir}/texmf-dist/tex/latex/pst-ob3d/

%files -n texlive-pst-ob3d-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-ob3d/

%files -n texlive-pst-ode
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-ode/
%{_texdir}/texmf-dist/tex/generic/pst-ode/
%{_texdir}/texmf-dist/tex/latex/pst-ode/

%files -n texlive-pst-ode-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-ode/

%files -n texlive-pst-optexp
%license lppl1.3.txt
%{_texdir}/texmf-dist/dvips/pst-optexp/
%{_texdir}/texmf-dist/makeindex/pst-optexp/
%{_texdir}/texmf-dist/tex/latex/pst-optexp/

%files -n texlive-pst-optexp-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/pst-optexp/

%files -n texlive-pst-optic
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-optic/
%{_texdir}/texmf-dist/tex/latex/pst-optic/

%files -n texlive-pst-optic-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-optic/

%files -n texlive-pst-osci
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-osci/
%{_texdir}/texmf-dist/tex/latex/pst-osci/

%files -n texlive-pst-osci-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-osci/

%files -n texlive-pst-ovl
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-ovl/
%{_texdir}/texmf-dist/tex/generic/pst-ovl/
%{_texdir}/texmf-dist/tex/latex/pst-ovl/

%files -n texlive-pst-ovl-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-ovl/

%files -n texlive-pst-pad
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-pad/
%{_texdir}/texmf-dist/tex/latex/pst-pad/

%files -n texlive-pst-pad-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-pad/

%files -n texlive-pst-pdgr
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-pdgr/
%{_texdir}/texmf-dist/tex/latex/pst-pdgr/

%files -n texlive-pst-pdgr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-pdgr/

%files -n texlive-pst-perspective
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/pst-perspective/
%{_texdir}/texmf-dist/tex/latex/pst-perspective/

%files -n texlive-pst-perspective-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/pst-perspective/

%files -n texlive-pst-platon
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pst-platon/

%files -n texlive-pst-platon-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-platon/

%files -n texlive-pst-plot
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-plot/
%{_texdir}/texmf-dist/tex/latex/pst-plot/

%files -n texlive-pst-plot-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-plot/

%files -n texlive-pst-poly
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-poly/
%{_texdir}/texmf-dist/tex/latex/pst-poly/

%files -n texlive-pst-poly-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-poly/

%files -n texlive-pst-pulley
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/pst-pulley/
%{_texdir}/texmf-dist/tex/latex/pst-pulley/

%files -n texlive-pst-pulley-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/pst-pulley/

%files -n texlive-pst-qtree
%license gpl.txt
%{_texdir}/texmf-dist/tex/generic/pst-qtree/
%{_texdir}/texmf-dist/tex/latex/pst-qtree/

%files -n texlive-pst-qtree-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/generic/pst-qtree/

%files -n texlive-pst-rubans
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-rubans/
%{_texdir}/texmf-dist/tex/latex/pst-rubans/

%files -n texlive-pst-rubans-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-rubans/

%files -n texlive-pst-sigsys
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-sigsys/
%{_texdir}/texmf-dist/tex/latex/pst-sigsys/

%files -n texlive-pst-sigsys-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-sigsys/

%files -n texlive-pst-slpe
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-slpe/
%{_texdir}/texmf-dist/tex/generic/pst-slpe/
%{_texdir}/texmf-dist/tex/latex/pst-slpe/

%files -n texlive-pst-slpe-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-slpe/

%files -n texlive-pst-solarsystem
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-solarsystem/
%{_texdir}/texmf-dist/tex/generic/pst-solarsystem/
%{_texdir}/texmf-dist/tex/latex/pst-solarsystem/

%files -n texlive-pst-solarsystem-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-solarsystem/

%files -n texlive-pst-solides3d
%license lppl1.3.txt
%{_texdir}/texmf-dist/dvips/pst-solides3d/
%{_texdir}/texmf-dist/tex/generic/pst-solides3d/
%{_texdir}/texmf-dist/tex/latex/pst-solides3d/

%files -n texlive-pst-solides3d-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/pst-solides3d/

%files -n texlive-pst-soroban
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pst-soroban/

%files -n texlive-pst-soroban-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-soroban/

%files -n texlive-pst-spectra
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-spectra/
%{_texdir}/texmf-dist/tex/generic/pst-spectra/
%{_texdir}/texmf-dist/tex/latex/pst-spectra/

%files -n texlive-pst-spectra-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-spectra/

%files -n texlive-pst-spirograph
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-spirograph/
%{_texdir}/texmf-dist/tex/generic/pst-spirograph/
%{_texdir}/texmf-dist/tex/latex/pst-spirograph/

%files -n texlive-pst-spirograph-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-spirograph/

%files -n texlive-pst-stru
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-stru/
%{_texdir}/texmf-dist/tex/latex/pst-stru/

%files -n texlive-pst-stru-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-stru/

%files -n texlive-pst-support-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-support/

%files -n texlive-pst-text
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-text/
%{_texdir}/texmf-dist/tex/generic/pst-text/
%{_texdir}/texmf-dist/tex/latex/pst-text/

%files -n texlive-pst-text-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-text/

%files -n texlive-pst-thick
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-thick/
%{_texdir}/texmf-dist/tex/latex/pst-thick/

%files -n texlive-pst-thick-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-thick/

%files -n texlive-pst-tools
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-tools/
%{_texdir}/texmf-dist/tex/generic/pst-tools/
%{_texdir}/texmf-dist/tex/latex/pst-tools/

%files -n texlive-pst-tools-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-tools/

%files -n texlive-pst-tree
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/pst-tree/
%{_texdir}/texmf-dist/tex/latex/pst-tree/

%files -n texlive-pst-tree-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-tree/

%files -n texlive-pst-tvz
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/pst-tvz/
%{_texdir}/texmf-dist/tex/latex/pst-tvz/

%files -n texlive-pst-tvz-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/pst-tvz/

%files -n texlive-pst-uml
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pst-uml/

%files -n texlive-pst-uml-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-uml/

%files -n texlive-pst-vectorian
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-vectorian/
%{_texdir}/texmf-dist/tex/latex/pst-vectorian/

%files -n texlive-pst-vectorian-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pst-vectorian/

%files -n texlive-pst-vowel
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pst-vowel/

%files -n texlive-pst-vowel-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pst-vowel/

%files -n texlive-pst-vue3d
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pst-vue3d/
%{_texdir}/texmf-dist/tex/generic/pst-vue3d/
%{_texdir}/texmf-dist/tex/latex/pst-vue3d/

%files -n texlive-pst-vue3d-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pst-vue3d/

%files -n texlive-pstricks
%license lppl1.3.txt
%{_texdir}/texmf-dist/dvips/pstricks/
%{_texdir}/texmf-dist/tex/generic/pstricks/
%{_texdir}/texmf-dist/tex/latex/pstricks/

%files -n texlive-pstricks-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/pstricks/

%files -n texlive-pstricks-add
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/pstricks-add/
%{_texdir}/texmf-dist/tex/generic/pstricks-add/
%{_texdir}/texmf-dist/tex/latex/pstricks-add/

%files -n texlive-pstricks-add-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/pstricks-add/

%files -n texlive-pstricks_calcnotes-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pstricks_calcnotes/

%files -n texlive-pracjourn
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/pracjourn/

%files -n texlive-pracjourn-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/pracjourn/

%files -n texlive-procIAGssymp
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/procIAGssymp/

%files -n texlive-procIAGssymp-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/procIAGssymp/

%files -n texlive-proposal
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/proposal/

%files -n texlive-proposal-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/proposal/

%files -n texlive-ptptex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ptptex/

%files -n texlive-ptptex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ptptex/

%files -n texlive-psu-thesis
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/psu-thesis/
%{_texdir}/texmf-dist/tex/latex/psu-thesis/

%files -n texlive-psu-thesis-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/psu-thesis/

%files -n texlive-pseudocode
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/pseudocode/

%files -n texlive-pseudocode-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/pseudocode/

%files -n texlive-ptext
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/xelatex/ptext/

%files -n texlive-ptext-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/xelatex/ptext/

%files -n texlive-prooftrees-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/prooftrees/

%files -n texlive-prooftrees
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/prooftrees/

%files -n texlive-pst-cie-doc
%license lppl.txt
%{_texdir}/texmf-dist/doc/generic/pst-cie/

%files -n texlive-pst-cie
%license lppl.txt
%{_texdir}/texmf-dist/dvips/pst-cie/
%{_texdir}/texmf-dist/tex/generic/pst-cie/
%{_texdir}/texmf-dist/tex/latex/pst-cie/

%files -n texlive-ptex-fonts
%license bsd.txt
%{_texdir}/texmf-dist/fonts/source/ptex-fonts/
%{_texdir}/texmf-dist/fonts/tfm/ptex-fonts/
%{_texdir}/texmf-dist/fonts/vf/ptex-fonts/

%files -n texlive-ptex-fonts-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/fonts/ptex-fonts/

%files -n texlive-ptex-base
%license bsd.txt
%{_texdir}/texmf-dist/tex/ptex/ptex-base/

%files -n texlive-ptex-base-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/ptex/ptex-base/

%files -n texlive-pst-arrow
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/generic/pst-arrow/
%{_texdir}/texmf-dist/tex/generic/pst-arrow/
%{_texdir}/texmf-dist/tex/latex/pst-arrow/

%files -n texlive-pst-geometrictools
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/generic/pst-geometrictools/
%{_texdir}/texmf-dist/tex/latex/pst-geometrictools/
%{_texdir}/texmf-dist/tex/generic/pst-geometrictools/

%files -n texlive-pst-poker
%license lgpl.txt
%doc %{_texdir}/texmf-dist/doc/latex/pst-poker/
%{_texdir}/texmf-dist/tex/latex/pst-poker/

%files -n texlive-pstring
%license pd.txt
%doc %{_texdir}/texmf-dist/doc/latex/pstring/
%{_texdir}/texmf-dist/tex/latex/pstring/

%files -n texlive-pst-rputover
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/generic/pst-rputover/
%{_texdir}/texmf-dist/tex/generic/pst-rputover/
%{_texdir}/texmf-dist/tex/latex/pst-rputover/

%files -n texlive-pst-shell
%license lppl.txt
%doc %{_texdir}/texmf-dist/doc/generic/pst-shell/
%{_texdir}/texmf-dist/dvips/pst-shell/
%{_texdir}/texmf-dist/tex/generic/pst-shell/
%{_texdir}/texmf-dist/tex/latex/pst-shell/

%files -n texlive-pst-vehicle
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/generic/pst-vehicle/
%{_texdir}/texmf-dist/tex/latex/pst-vehicle/
%{_texdir}/texmf-dist/tex/generic/pst-vehicle/

%files -n texlive-pxtatescale
%doc %{_texdir}/texmf-dist/doc/latex/pxtatescale/
%{_texdir}/texmf-dist/tex/latex/pxtatescale/

%files -n texlive-pxufont
%doc %{_texdir}/texmf-dist/doc/latex/pxufont/
%{_texdir}/texmf-dist/fonts/tfm/public/pxufont/
%{_texdir}/texmf-dist/fonts/vf/public/pxufont/
%{_texdir}/texmf-dist/tex/latex/pxufont/

%files -n texlive-pst-antiprism
%license lppl.txt
%{_texdir}/texmf-dist/dvips/pst-antiprism/
%{_texdir}/texmf-dist/tex/generic/pst-antiprism/
%{_texdir}/texmf-dist/tex/latex/pst-antiprism/
%doc %{_texdir}/texmf-dist/doc/generic/pst-antiprism/

%files -n texlive-pst-calculate
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/pst-calculate/
%doc %{_texdir}/texmf-dist/doc/generic/pst-calculate/

%files -n texlive-pst-contourplot
%license lppl.txt
%{_texdir}/texmf-dist/tex/generic/pst-contourplot/
%{_texdir}/texmf-dist/tex/latex/pst-contourplot/
%doc %{_texdir}/texmf-dist/doc/generic/pst-contourplot/

%files -n texlive-pst-dart
%license lppl.txt
%{_texdir}/texmf-dist/tex/generic/pst-dart/
%{_texdir}/texmf-dist/tex/latex/pst-dart/
%doc %{_texdir}/texmf-dist/doc/generic/pst-dart/

%files -n texlive-pst-spinner
%license lppl.txt
%{_texdir}/texmf-dist/dvips/pst-spinner/
%{_texdir}/texmf-dist/tex/generic/pst-spinner/
%{_texdir}/texmf-dist/tex/latex/pst-spinner/
%doc %{_texdir}/texmf-dist/doc/generic/pst-spinner/

%files -n texlive-pythonhighlight
%license bsd.txt
%{_texdir}/texmf-dist/tex/latex/pythonhighlight/
%doc %{_texdir}/texmf-dist/doc/latex/pythonhighlight/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
